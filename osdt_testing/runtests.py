import contextlib
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
unittest.TestLoader.sortTestMethodsUsing = None
OUTPUT_PATH = "osdt_examples/osdt_testing/files/"
def run_tests(*test_cases):
    report="test report"
    for test_case in test_cases:
        s = unittest.makeSuite(test_case)
        with io.StringIO() as buf:
            # run the tests
            with contextlib.redirect_stdout(buf):
                unittest.TextTestRunner(stream=buf,verbosity=2).run(s)
            # process (in this case: print) the results
            test_report='%s' % buf.getvalue()
            report=report+"\n"+test_report
    return report
def main(path="osdt_examples/sysfiles/argtest3.yaml", key="system" ):  ##.ball.__name__, read_file=""
    remove_path = osdt.get_path(OUTPUT_PATH)
    if os.path.exists(remove_path):
        shutil.rmtree(remove_path)
    else:
        os.makedirs(remove_path)
    log.info("pre-move: "+osdt.get_run_params().log_file)
    osdt.change_output_path(remove_path, clear_old_log=True)
   # osdt.logger.log_enabled(False)
    report=run_tests(fileio_tests.TestStringMethods)
    print(report)
    #fileio_tests.rt()
    #unittest.main()
  #  t=fileio_tests.TestStringMethods()
  #  t.run()
   # fileio.run_tests()



