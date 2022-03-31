import argparse
import contextlib
import inspect
import io
import os
import shutil
import sys
import unittest
import logging as log
import osdt

osdt.enable_user_data(False)

OUTPUT_DIR = "files/"
TEST_OUTPUT_SUBDIR = "files/"
TEST_FILE_DIR = OUTPUT_DIR+TEST_OUTPUT_SUBDIR
APPEND_PATHS = ["tests","models"]
TEST_MODULE_PARENT = "tests"
TEST_MODULE_PATH = "tests"

print_log = True

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

class StreamWithStdOut:
    def __init__(self, stream):
        self.curr_line = ""
        self.stream = stream
    def write(self, data):
        self.curr_line = self.curr_line + data
        if "\n" in self.curr_line:
            if len(self.curr_line)>2:
                log.info(self.curr_line.rstrip("\n"))
            self.curr_line=""
        self.stream.write(data)
        self.stream.flush()
    def writelines(self, datas):
        for line in datas:
            log.info(line.rstrip("\n"))
        self.stream.writelines(datas)
        self.stream.flush()
    def __getattr__(self, attr):
        return getattr(self.stream, attr)

def run_module_tests(*modules):
    report = ""
    for module in modules:
        module_header = "\n" + osdt.logger.create_header(
            module.__name__, bar_char="#") + "\n"
        log.info("testing: "+module.__name__)
        clear_test_files()
        alltests = unittest.TestSuite()
        report = report +  module_header
        module_tests = get_module_tests(module)
        for test in module_tests:
            alltests.addTest(unittest.makeSuite(test))
        else:
            with io.StringIO() as buf:
                if print_log:
                    st = StreamWithStdOut(buf)
                else:
                    st = buf

                unittest.TextTestRunner(stream=st, verbosity=2).run(alltests)
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
    remove_path = osdt.get_path(TEST_FILE_DIR)
    if os.path.exists(remove_path):
        print("removing: "+remove_path)
        shutil.rmtree(remove_path)
    else:
        os.makedirs(remove_path)

def get_test_modules():
    test_modules=[]
    module_files=os.listdir(TEST_MODULE_PATH)
    for module_file in module_files:
        if module_file.endswith(osdt.defs.PYTHON_FILE_EXT):
            module_name = module_file.rstrip(osdt.defs.PYTHON_FILE_EXT)
            full_module = TEST_MODULE_PARENT+"."+module_name
            print(full_module)

            #__import__(full_module)
            #module=sys.modules[full_module]
            module=osdt.utils.get_module_from_name(module_name)
            test_modules.append(module)
    return test_modules

def run_tests():
    log.info("\n\n"+osdt.logger.create_header("Test Log",bar_char="#")+"\n\n")
    test_modules=get_test_modules()
    report = run_module_tests(*test_modules)
    osdt.log_enabled(True)
    log.info("unit testing complete:\n" + report)

def setup_paths():
    test_root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(test_root)
    log.info("test root: " + test_root)
    for append_path in APPEND_PATHS:
        append_abs_path = os.path.abspath(append_path)
        sys.path.append(append_abs_path)
    osdt.change_output_path(OUTPUT_DIR)
    print(os.path.abspath("."))

def get_log_conf():
    conf = osdt.user.UserSettings()
    conf.log_msg_format="%(levelname)-5.5s | %(message)s"
    conf.log_msg_format_debug="%(levelname)-5.5s | %(message)s | %(filename)s:%(lineno)s"
    osdt.logger.configure_logger(conf=conf)

def main(args):
    global print_log
    setup_paths()
    if not args.date:
        get_log_conf()
        log.info("test")
    print_log = args.log
    osdt.log_enabled(print_log)
    run_tests()


if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--log", action="store_true",default=False)
    parser.add_argument("--date", action="store_true",default=False)
    args=parser.parse_args()
    main(args)