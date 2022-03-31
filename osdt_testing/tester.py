import contextlib
import inspect
import io
import os
import shutil
import unittest
import logging as log
import osdt


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

def run_module_tests(*modules):
    report = ""
    for module in modules:
        alltests = unittest.TestSuite()
        report = report + "\n" + osdt.logger.create_header(
            module.__name__, bar_char="#") + "\n"
        module_tests = get_module_tests(module)
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

def get_module_tests(module):
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

def clear_test_files():  ##.ball.__name__, read_file=""
    remove_path = osdt.get_path(OUTPUT_PATH)
    if os.path.exists(remove_path):
        shutil.rmtree(remove_path)
    else:
        os.makedirs(remove_path)

def run_tests():
    log.info("pre-move: " + osdt.get_run_params().log_file)
    osdt.change_output_path(remove_path, clear_old_log=True)
    report = run_tests(fileio_tests, environment_tests)
    log.info("unit testing complete:\n" + report)