import osdt
import contextlib
import copy
import io
import os
import shutil
import unittest
import logging as log
import osdt
from test_models import ball


def create_system(**args):
    ball_sys=ball.create(**args)
    return ball_sys



class SystemTests(unittest.TestCase):
    def setUp(self) -> None:
        osdt.enable_user_data(False)

    def test_auto_add_systems(self):
        osdt.clear()
        system1 = create_system()
        self.assertEqual(len(osdt.get_systems()),1)
        system2 = create_system()
        self.assertEqual(len(osdt.get_systems()),2)

    def test_add_systems(self):
        osdt.clear()
        system1 = create_system(add=False)
        system2 = create_system(add=False)

        self.assertEqual(len(osdt.get_systems()), 0)
        osdt.add_systems(system1,system2)
        self.assertEqual(len(osdt.get_systems()), 2)

    def test_add_duplicates(self):
        osdt.clear()
        system1 = create_system()
        base_id = system1.get_id()
        system2 = create_system()
        sys_map=osdt.get_systems(map=True)
        self.assertTrue(base_id+"_1" in sys_map)
        self.assertTrue(base_id + "_2" in sys_map)

