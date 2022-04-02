"""Bouncing ball model"""
import os.path
import sys
import osdt
from osdt import load_call

def main(path="call_files/systems.yaml",systems={},calls={}):  ##.ball.__name__, read_file=""
	print(osdt.get_path(path))
	print(systems)
	for system_id in systems:
		system_call = systems[system_id]
		new_sys = load_call(path,system_call)#,state=dubins_controller.State(velocity=0.75,turn=1.0))
	for call_map in calls:
		for call in call_map:
			args =call_map[call]
			load_call(path,call,**args)

	osdt.run()

	osdt.construct_figures("call_files/figure.yaml","figure2")
