import contextlib
import copy
import io
import os
import shutil
import unittest
import logging as log
import osdt
from test_models import ball
from tester import OUTPUT_DIR,TEST_OUTPUT_SUBDIR
SAVED_OBJ=TEST_OUTPUT_SUBDIR+"saved_obj"
LOAD_OBJ = OUTPUT_DIR+SAVED_OBJ+osdt.defs.OSDT_FILE_EXT
SAVED_ENV=TEST_OUTPUT_SUBDIR+"saved_env"
LOAD_ENV = OUTPUT_DIR+SAVED_ENV

ball_state = ball.State()
ball_state2 = ball.State(y_position=999.99)

ball_sys = ball.create(state=ball_state)
env=osdt.get_environment()

class SaveTests(unittest.TestCase):
    def test_save_obj(self):
        osdt.save_obj(ball_sys, SAVED_OBJ)
        self.assertTrue(os.path.exists(osdt.get_path(LOAD_OBJ)))

    def test_save_env(self):
        osdt.clear()
        osdt.add_systems(ball_sys)
        osdt.save_env(SAVED_ENV,overwrite=True)
        self.assertTrue(os.path.exists(osdt.get_path(LOAD_ENV)))

class LoadTests(unittest.TestCase):
    def compare_states(self,orig,loaded):
        self.assertEqual(len(orig.__dict__), len(loaded.__dict__))
        for key in orig.__dict__:
            self.assertEqual(orig.__dict__[key], loaded.__dict__[key])
    def test_load_obj(self):
        loaded_sys = osdt.load_obj(LOAD_OBJ)
        loaded = loaded_sys.x()
        orig= ball_state
        self.compare_states(orig,loaded)
    def test_load_env(self):
        osdt.clear()
        loaded = osdt.load_env(LOAD_ENV)
        sys1 = loaded.get_system(ball_sys.get_id())
        self.compare_states(ball_sys.x(),sys1.x())

class LoadTestsBad(unittest.TestCase):
    def compare_states(self,orig,loaded):
        self.assertEqual(len(orig.__dict__), len(loaded.__dict__))
        for key in orig.__dict__:
            self.assertEqual(orig.__dict__[key], loaded.__dict__[key])
    def test_load_obj(self):
        loaded_sys = osdt.load_obj(LOAD_OBJ)
        loaded = loaded_sys.x()
        orig= copy.deepcopy(ball_state)
        orig.y_position=43243.0
        self.compare_states(orig,loaded)
    def test_load_env(self):
        osdt.clear()
        loaded = osdt.load_env(LOAD_ENV)
        sys1 = loaded.get_system(ball_sys.get_id())
        #self.compare_states(ball_sys.x(),sys1.x())
        self.compare_states(ball_state2, sys1.x())
