#  Copyright (c) 2015 SONATA-NFV, 5GTANGO, Paderborn University
# ALL RIGHTS RESERVED.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Neither the name of the SONATA-NFV, 5GTANGO, Paderborn University
# nor the names of its contributors may be used to endorse or promote
# products derived from this software without specific prior written
# permission.
#
# This work has been performed in the framework of the SONATA project,
# funded by the European Commission under Grant number 671517 through
# the Horizon 2020 and 5G-PPP programmes. The authors would like to
# acknowledge the contributions of their colleagues of the SONATA
# partner consortium (www.sonata-nfv.eu).
#
# This work has also been performed in the framework of the 5GTANGO project,
# funded by the European Commission under Grant number 761493 through
# the Horizon 2020 and 5G-PPP programmes. The authors would like to
# acknowledge the contributions of their colleagues of the SONATA
# partner consortium (www.5gtango.eu).

import os
import tempfile
import argparse
import logging
import coloredlogs
import time
import shutil
import subprocess
from tngsdk.benchmark.experiment import ServiceExperiment, FunctionExperiment
from tngsdk.benchmark.generator.sonata \
                import SonataServiceConfigurationGenerator
from tngsdk.benchmark.generator.tango \
                import TangoServiceConfigurationGenerator
from tngsdk.benchmark.executor import Executor
from tngsdk.benchmark.helper import read_yaml, get_prometheus_path
from tngsdk.benchmark.ietf import IetfBmwgVnfBD_Generator
from tngsdk.benchmark.resultprocessor.vimemu import VimemuResultProcessor
from tngsdk.benchmark.logger import TangoLogger


logging.getLogger("urllib3").setLevel(logging.WARNING)


def setup_logging(args):
    """
    Configure logging.
    """
    log_level = logging.INFO
    # get loglevel from environment or --loglevel
    log_level_str = os.environ.get("LOGLEVEL", "INFO")
    if args.log_level:  # overwrite if present
        log_level_str = args.log_level
    # parse
    log_level_str = str(log_level_str).lower()
    if log_level_str == "debug":
        log_level = logging.DEBUG
    elif log_level_str == "info":
        log_level = logging.INFO
    elif log_level_str == "warning":
        log_level = logging.WARNING
    elif log_level_str == "error":
        log_level = logging.ERROR
    else:
        print("Loglevel '{}' unknown.".format(log_level_str))
    # if "-v" is there set to debug
    if args.verbose:
        log_level = logging.DEBUG
    # select logging mode
    log_json = os.environ.get("LOGJSON", args.logjson)
    # configure all TangoLoggers
    TangoLogger.reconfigure_all_tango_loggers(
        log_level=log_level, log_json=log_json)


class ProfileManager(object):
    """
    Main component class.
    """

    def __init__(self, args):
        self.logger = TangoLogger.getLogger(__name__)
        self.start_time = time.time()
        self.service_experiments = list()
        self.function_experiments = list()
        self.args = args
        self.args.debug = self.args.verbose
        self.args.ped = os.path.join(os.getcwd(), self.args.ped)
        # load config file: try different paths
        for path in [os.path.abspath(os.path.expanduser(args.configfile)),
                     os.path.abspath(".tng-bench.conf"),
                     os.path.abspath("config.yml")]:
            try:
                self.args.config = self._load_config(path)
                break
            except BaseException as ex:
                self.logger.error(ex)
                self.args.config = None
        if self.args.config is None:
            print("Connot run without configuration.")
            exit(1)

        # logging setup
        coloredlogs.install(level="DEBUG" if args.verbose else "INFO")
        self.logger.info("5GTANGO benchmarking/profiling tool initialized")
        self.logger.debug("Arguments: %r" % self.args)

    def run(self):
        """
        Run son-profile
        :return:
        """
        self.check_rd_existence()
        self.populate_experiments()
        # trigger experiment execution
        self.cgen = self.load_generator()
        if self.cgen is None:
            return
        self.generate_experiments()
        if not self.args.no_prometheus:
            self.start_prometheus_monitoring()
        self.execute_experiments()
        self.process_results()
        self.copy_ped()
        if not self.args.no_prometheus:
            self.stop_prometheus_monitoring()

    def check_rd_existence(self):
        if os.path.exists(self.args.result_dir):
            self.logger.info("Found old results: {}"
                             .format(self.args.result_dir))
            # ask for overwrite (if not -y/--force-yes)
            if not self.args.force_yes:
                # ask user
                ui = input("Do you want to overwrite '{}'? (y/n/default: y)"
                           .format(self.args.result_dir))
                if "n" in ui or "N" in ui:
                    return
            # delte old results
            self.logger.info("Overwriting old results: {}"
                             .format(self.args.result_dir))
            shutil.rmtree(self.args.result_dir)
            # also clean prometheus data (if present, rquires sudo)
            if not self.args.no_prometheus:
                try:
                    pm_path = get_prometheus_path()
                    self.logger.info("Removing Prometheus data: {}"
                                     .format(pm_path))
                    subprocess.call(["./clean.sh"], cwd=pm_path)
                except BaseException as ex:
                    self.logger.warning("Couldn't remove Prometheus data: {}"
                                        .format(ex))

    def start_prometheus_monitoring(self):
        try:
            pm_path = get_prometheus_path()
            self.logger.info("Starting Prometheus 'docker-compose up in:' {}"
                             .format(pm_path))
            subprocess.call(["docker-compose", "up", "-d"], cwd=pm_path)
        except BaseException as ex:
            self.logger.warning("Couldn't start Prometheus. Skipping it. ({})"
                                .format(ex))

    def stop_prometheus_monitoring(self):
        try:
            pm_path = get_prometheus_path()
            self.logger.info("Stopping Prometheus 'docker-compose down in:' {}"
                             .format(pm_path))
            subprocess.call(["docker-compose", "down"], cwd=pm_path)
        except BaseException as ex:
            self.logger.warning("Couldn't stop Prometheus. Skipping it. ({})"
                                .format(ex))

    def populate_experiments(self):
        if self.args.no_population:
            print("Skipping population: --no-population")
            return
        # try to load PED file
        self.ped = self._load_ped_file(self.args.ped)
        self._validate_ped_file(self.ped)
        # load and populate experiment specifications
        (self.service_experiments,
         self.function_experiments) = (
             self._generate_experiment_specifications(self.ped))

    def load_generator(self):
        # select and instantiate configuration generator
        cgen = None
        if self.args.service_generator == "sonata":
            cgen = SonataServiceConfigurationGenerator(self.args)
        if self.args.service_generator == "eu.5gtango":
            cgen = TangoServiceConfigurationGenerator(self.args)
        else:
            self.logger.error(
                "Unknown service configuration generator '{0}'. Exit 1."
                .format(self.args.service_generator))
            exit(1)
        if cgen is None:
            self.logger.error("Service conf. generator instantiation failed.")
            exit(1)
        return cgen

    def generate_experiments(self):
        if self.args.no_generation:
            print("Skipping generation: --no-generation")
            return
        if self.cgen is None:
            raise BaseException("No generator loaded.")
        # generate one service configuration for each experiment based
        # on the service referenced in the PED file.
        # outputs are annotated to
        # service_experiments.experiment.configurations
        #    .run_id
        #    .project_path
        #    .package_path
        self.cgen.generate(
            os.path.join(  # ensure that the reference is an absolute path
                 os.path.dirname(
                     self.ped.get("ped_path", "/")),
                 self.ped.get("service_package")),
            self.function_experiments,
            self.service_experiments)
        # display generator statistics
        if not self.args.no_display:
            self.cgen.print_generation_and_packaging_statistics()

    def execute_experiments(self):
        if self.args.no_execution:
            print("Skipping execution: --no-execution")
            return
        # create an executor
        exe = Executor(self.args, self.service_experiments)
        # prepare
        exe.setup()
        # run
        exe.run()
        # clean
        exe.teardown()

    def process_results(self):
        if self.args.no_result:
            self.logger.info("Skipping results: --no-result")
            return
        # create result prcessor
        rp_list = list()
        rp_list.append(IetfBmwgVnfBD_Generator(
            self.args, self.service_experiments))
        rp_list.append(VimemuResultProcessor(
            self.args, self.service_experiments))
        self.logger.info("Prepared {} result processor(s)"
                         .format(len(rp_list)))
        # process results
        for rp in rp_list:
            self.logger.info("Running result processor '{}'".format(rp))
            rp.run()

    def copy_ped(self):
        """
        Copy the used PED file to the result folder
        to have a reference of the used experiment parameters.
        """
        src = self.args.ped
        dst = os.path.join(self.args.result_dir, "original_ped.yml")
        try:
            self.logger.info("Copying PED ({}) to folder {}"
                             .format(src, dst))
            shutil.copyfile(src, dst)
        except BaseException as ex:
            self.logger.error("Couldn't copy used PED to result folder.")
            self.logger.debug(ex)

    def _load_config(self, path):
        try:
            self.logger.info("Using config: {}".format(path))
            return read_yaml(path)
        except BaseException as ex:
            self.logger.exception("Couldn't read config file: '{}'. Abort."
                                  .format(path))
            self.logger.debug(ex)
            raise BaseException("Config not found.")

    def _load_ped_file(self, ped_path):
        """
        Loads the specified PED file.
        :param ped_path: path to file
        :return: dictionary
        """
        yml = None
        try:
            yml = read_yaml(ped_path)
            if yml is None:
                raise BaseException("PED file YAML error.")
        except BaseException:
            self.logger.error("Couldn't load PED file %r. Abort." % ped_path)
            exit(1)
        # add path annotation to ped file (simpler
        # handling of referenced artifacts)
        yml["ped_path"] = ped_path
        self.logger.info("Loaded PED file %r." % ped_path)
        return yml

    def _validate_ped_file(self, input_ped):
        """
        Semantic validation of PED file contents.
        Check for all things we need to have in PED file.
        :param input_ped: ped dictionary
        :return: None
        """
        try:
            if "service_package" not in input_ped:
                raise BaseException("No service_package field found.")
            # TODO extend this with PED fields that are REQUIRED
        except BaseException:
            self.logger.exception("PED file verification error:")

    def _generate_experiment_specifications(self, input_ped):
        """
        Create experiment objects based on the contents of the PED file.
        :param input_ped: ped dictionary
        :return: service experiments list, function experiments list
        """
        service_experiments = list()
        function_experiments = list()

        # service experiments
        for e in input_ped.get("service_experiments", []):
            if e.get("disabled"):
                continue  # skip disabled experiments
            e_obj = ServiceExperiment(
                self.args, e, input_ped.get("service_package"))
            e_obj.populate()
            service_experiments.append(e_obj)

        # function experiments
        for e in input_ped.get("function_experiments", []):
            if e.get("disabled"):
                continue  # skip disabled experiments
            e_obj = FunctionExperiment(
                self.args, e, input_ped.get("service_package"))
            e_obj.populate()
            function_experiments.append(e_obj)

        return service_experiments, function_experiments


def parse_args(manual_args=None,
               ped_mandatory=True,
               result_dir_mandatory=False):
    """
    CLI interface definition.
    :return:
    TODO move to cli.py module
    """
    parser = argparse.ArgumentParser(
        description="Manage and control VNF and "
        + "service profiling experiments.")

    parser.add_argument(
        "-v",
        "--verbose",
        help="Increases logging level to debug.",
        required=False,
        default=False,
        dest="verbose",
        action="store_true")

    parser.add_argument(
        "--loglevel",
        help="Directly specify loglevel. Default: INFO",
        required=False,
        default=None,
        dest="log_level")

    parser.add_argument(
        "--logjson",
        help="Use 5GTANGO JSON-based logging. Default: False",
        required=False,
        default=False,
        dest="logjson",
        action="store_true")

    parser.add_argument(
        "-p",
        "--ped",
        help="PED file to be used for profiling run",
        required=ped_mandatory,
        default="",
        dest="ped")

    parser.add_argument(
        "-c",
        "--config",
        help="Config file to be used, e.g., defining the execution platforms."
        + "Default: ~/.tng-bench.conf",
        required=False,
        default="~/.tng-bench.conf",
        dest="configfile")

    parser.add_argument(
        "--work-dir",
        help="Dictionary for generated artifacts,"
        + " e.g., profiling packages. Will use a temporary"
        + " folder as default.",
        required=False,
        default=tempfile.mkdtemp(),
        dest="work_dir")

    parser.add_argument(
        "-rd",
        "--result-dir",
        help="Dictionary for measured results,"
        + " e.g., logfiles, monitoring data. Default: '(cwd)/results/'",
        required=result_dir_mandatory,
        default="results",
        dest="result_dir")

    parser.add_argument(
        "--no-generation",
        help="Skip profiling package generation step.",
        required=False,
        default=False,
        dest="no_generation",
        action="store_true")

    parser.add_argument(
        "--no-population",
        help="Skip experiment population step.",
        required=False,
        default=False,
        dest="no_population",
        action="store_true")

    parser.add_argument(
        "--no-execution",
        help="Skip profiling execution step.",
        required=False,
        default=False,
        dest="no_execution",
        action="store_true")

    parser.add_argument(
        "--no-result",
        help="Skip result processing step.",
        required=False,
        default=False,
        dest="no_result",
        action="store_true")

    parser.add_argument(
        "--validation",
        help="Skip all package validation steps.",
        required=False,
        default=True,
        dest="skip_validation",
        action="store_false")

    parser.add_argument(
        "--hold",
        help=("Stop when experiment is started and" +
              " wait for user input (helps for debugging)."),
        required=False,
        default=False,
        dest="hold_and_wait_for_user",
        action="store_true")

    parser.add_argument(
        "--max-experiments",
        help=("Maximum number of experiments to generate" +
              " irrespective of PED def. (helps for debugging)."),
        required=False,
        default=None,
        dest="max_experiments")

    parser.add_argument(
        "--no-display",
        help="Disable additional outputs.",
        required=False,
        default=False,
        dest="no_display",
        action="store_true")

    parser.add_argument(
        "--generator",
        help="Service configuration generator to be used."
        + " Default: 'eu.5gtango'",
        required=False,
        default="eu.5gtango",
        dest="service_generator")

    parser.add_argument(
        "--ibbd",
        help="Dictionary for generated IETF BMWG"
        + " 'benchmarking secriptors'."
        + " Default: None",
        required=False,
        default=None,
        dest="ibbd_dir")

    parser.add_argument(
        "-y",
        "--force-yes",
        help="Answer all user questions that might appear with: yes.",
        required=False,
        default=False,
        dest="force_yes",
        action="store_true")

    parser.add_argument(
        "--no-prometheus",
        help="Do not launch Prometheus automatically.",
        required=False,
        default=False,
        dest="no_prometheus",
        action="store_true")

    if manual_args is not None:
        return parser.parse_args(manual_args)
    return parser.parse_args()


def main(args=None):
    """
    Main entry point.
    """
    args = parse_args(args)
    setup_logging(args)
    p = ProfileManager(args)
    p.run()


def main_result_processor(args=None):
    """
    Additional entry to process existing results.
    """
    args = parse_args(args,
                      ped_mandatory=False,
                      result_dir_mandatory=True)
    # ensure that we skip generation and execution
    args.no_generation = True
    args.no_execution = True
    args.no_population = True
    setup_logging(args)
    p = ProfileManager(args)
    p.run()
