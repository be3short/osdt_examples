import traceback

import tester
import unittest,os,sys,copy,unittest,osdt
import logging as log



class SystemTests(unittest.TestCase):
    def test_manual_user_data_path(self):

        tester.restore_initial_modules(unittest, os, sys, copy, unittest, osdt,
                                       tester, log)
        osdt.enable_user_files(False,restore_defaults=True)
        loaded=False
        try:
            from user_test_model import sub_ball
            loaded = True
        except:
            pass

        self.assertFalse(loaded)
        osdt.get_user_data().path.append(os.path.join("files","not_on_path"))
        osdt.get_user_data().load_all()
        loaded=False
        try:
            from user_test_model import sub_ball
            loaded = True
        except:
            log.error("failed",traceback.format_exc())
        self.assertTrue(loaded)

    def test_auto_add_systems(self):
        osdt.enable_user_files(True)
        initial_modules = list(sys.path)
        osdt.enable_user_files(False,restore_defaults=True)
        current_modules = list(sys.path)
        changed_modules = []
        for mod in initial_modules:
            if mod not in current_modules:
                changed_modules.append(mod)
        log.info(changed_modules)
        osdt.enable_user_files(True)
        reloaded_modules = list(sys.path)
        self.assertEqual(len(current_modules)+len(changed_modules),len(reloaded_modules))
        same_modules = True
        for mod in initial_modules:
            if mod not in reloaded_modules:
                same_modules = False
        self.assertTrue(same_modules)



