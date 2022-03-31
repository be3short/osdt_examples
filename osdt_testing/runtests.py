import contextlib
import inspect
import io
import os
import shutil
import unittest
import logging as log
import osdt
from osdt_examples.models import ball, timer, point_mass,sensor,heater_system,heater_controller,dubins_vehicle,dubins_controller
from osdt import load_call
from osdt_examples.osdt_testing import fileio
from osdt_examples.osdt_testing import fileio_tests
from osdt_examples.osdt_testing import environment_tests
unittest.TestLoader.sortTestMethodsUsing = None
OUTPUT_PATH = "osdt_examples/osdt_testing/files/"


class ModuleMembers:
    def __init__(self,module):
        self.module = module
        self.member_map = ModuleMembers.get_full_member_map(self.module)
        self.member_map = self.get_sorted_member_map()

    def get_sorted_member_map(self):
        member_map = {}
        member_keys = list(self.member_map.keys())
        member_keys.sort(key=self.sort_by_line_no)
        for member_key in member_keys:
            member_map[member_key]=self.member_map[member_key]
        return member_map

    def sort_by_line_no(self, obj_key):
        obj = self.member_map[obj_key]
        source, line_no = inspect.findsource(obj)
        return line_no

    @staticmethod
    def get_full_member_map(module):
        members = inspect.getmembers(module)
        member_map = {}
        for member in members:
            member_name = member[0]
            member_obj = member[1]
            if not inspect.isbuiltin(member_obj) and inspect.isclass(
                    member_obj):
                member_map[member_name] = member_obj
        return member_map
    @staticmethod
    def get_member_map(module):
        module_members = ModuleMembers(module)
        member_map = module_members.member_map
        return member_map

def run_all_tests(*modules):
    report = ""
    for module in modules:
        alltests = unittest.TestSuite()
        report = report + "\n" + osdt.logger.create_header(
            module.__name__, bar_char="#") + "\n"
        module_tests = get_tests(module)
        for test in module_tests:
            alltests.addTest(unittest.makeSuite(test))
        with io.StringIO() as buf:
            # run the tests
            with contextlib.redirect_stdout(buf):
                unittest.TextTestRunner(stream=buf, verbosity=2).run(alltests)
            # process (in this case: print) the results
            test_report = '%s' % buf.getvalue()
            report = report + "\n" + test_report

    return report

def run_test_modules(*test_modules):
    report=""
    for module in test_modules:
        alltests = unittest.TestSuite()
        report = report + "\n" + osdt.logger.create_header(
            module.__name__, bar_char="#") + "\n"
        for test in module.TESTS:
            alltests.addTest(unittest.makeSuite(test))
        with io.StringIO() as buf:
            # run the tests
            with contextlib.redirect_stdout(buf):
                unittest.TextTestRunner(stream=buf, verbosity=2).run(alltests)
            # process (in this case: print) the results
            test_report = '%s' % buf.getvalue()
            report = report + "\n" + test_report
    return report

def run_tests(*test_cases):
    log.info("running unit tests")
    report=""
    alltests = unittest.TestSuite()

    for test_case in test_cases:
        #report=report+"\n"+osdt.logger.create_header(osdt.utils.get_full_obj_name(test_case),bar_char="#")+"\n"
        alltests.addTest(unittest.makeSuite(test_case))
        #s = unittest.makeSuite(test_case)
    with io.StringIO() as buf:
        # run the tests
        with contextlib.redirect_stdout(buf):
            unittest.TextTestRunner(stream=buf,verbosity=2).run(alltests)
        # process (in this case: print) the results
        test_report='%s' % buf.getvalue()
        report=report+"\n"+test_report
    log.info("unit testing complete:\n"+report+"\n")
    return report


def run_tests(*test_cases):
    log.info("running unit tests")
    report=""
    alltests = unittest.TestSuite()

    for test_case in test_cases:
        report=report+"\n"+osdt.logger.create_header(osdt.utils.get_full_obj_name(test_case),bar_char="#")+"\n"
        s = unittest.makeSuite(test_case)
        with io.StringIO() as buf:
            # run the tests
            with contextlib.redirect_stdout(buf):
                unittest.TextTestRunner(stream=buf,verbosity=2).run(s)
            # process (in this case: print) the results
            test_report='%s' % buf.getvalue()
            report=report+"\n"+test_report
    log.info("unit testing complete:\n"+report+"\n")
    return report

def add_tests(test_list, *tests):
    for test in tests:
        test_list.append(test)

def get_all_tests(*modules):
    all_tests = {}
    for module in modules:
        module_name = module.__name__
        module_tests=get_tests(module)
        all_tests[module_name]=module_tests

def get_tests(module):
    global mmap
    module_tests=[]
    member_map = ModuleMembers.get_member_map(module)
    module_name = module.__name__
    for member_name in member_map:
        member_obj = member_map[member_name]
        if not inspect.isbuiltin(member_obj) and inspect.isclass(member_obj):
            member_module = member_obj.__module__
            if member_module == module_name:
                module_tests.append(member_obj)
    return module_tests

def main(path="osdt_examples/sysfiles/argtest3.yaml", key="system" ):  ##.ball.__name__, read_file=""
    remove_path = osdt.get_path(OUTPUT_PATH)
    if os.path.exists(remove_path):
        shutil.rmtree(remove_path)
    else:
        os.makedirs(remove_path)
    log.info("pre-move: "+osdt.get_run_params().log_file)
    osdt.change_output_path(remove_path, clear_old_log=True)
   # osdt.logger.log_enabled(False)
    #report=run_tests(*fileio_tests.TESTS)
    #report=run_test_modules(fileio_tests)
    report=run_all_tests(fileio_tests,environment_tests)
    log.info("unit testing complete:\n"+report)
    #get_tests(fileio_tests)
    #log.info(str(inspect.get.getmembers(fileio_tests)))
    #print(report)
    #fileio_tests.rt()
    #unittest.main()
  #  t=fileio_tests.TestStringMethods()
  #  t.run()
   # fileio.run_tests()



