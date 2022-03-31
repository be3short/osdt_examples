import contextlib
import io
import os
import shutil
import unittest
import logging as log
import osdt
from osdt_examples.models import ball
TEST_DIR = "osdt_examples/osdt_testing/files/"
SAVED_OBJ="saved_obj"
LOAD_OBJ = TEST_DIR+SAVED_OBJ+osdt.defs.OSDT_FILE_EXT
SAVED_ENV="saved_env"
LOAD_ENV = TEST_DIR+SAVED_ENV

ball_state = ball.State()
ball_sys = ball.create(state=ball_state)
env=osdt.get_environment()

class SaveTests(unittest.TestCase):
    def test_save_obj(self):
        osdt.save_obj(ball_sys, SAVED_OBJ)
        self.assertTrue(os.path.exists(osdt.get_path(LOAD_OBJ)))
    def test_save_env(self):
        osdt.save_env(SAVED_ENV,overwrite=True)
        self.assertTrue(os.path.exists(osdt.get_path(LOAD_ENV)))

class LoadTests(unittest.TestCase):
    def test_load_obj(self):
        loaded_sys = osdt.load_obj(LOAD_OBJ)
        loaded = loaded_sys.x()
        orig= ball_state
        self.assertEqual(len(orig.__dict__), len(loaded.__dict__))
        for key in orig.__dict__:
              self.assertEqual(orig.__dict__[key],loaded.__dict__[key])
        return loaded
    def test_load_obj(self):
        osdt.clear()
        loaded = osdt.load_env(LOAD_ENV)
        sys1 = loaded.get_system(ball_sys.get_id())
        for key in ball_sys.x().__dict__:
            passed = passed and (
                        ball_sys.x().__dict__[key] == sys1.x().__dict__[key])
        return passed


TESTS = [SaveTests,LoadTests]

def run_tests( test_case ):
    report="test report"

    s = unittest.makeSuite(test_case)
    with io.StringIO() as buf:
        # run the tests
        with contextlib.redirect_stdout(buf):
            unittest.TextTestRunner(stream=buf,verbosity=2).run(s)
        # process (in this case: print) the results
        test_report='%s' % buf.getvalue()
        report=report+"\n"+test_report
    return report

def rt():
    print(run_tests(TestStringMethods))