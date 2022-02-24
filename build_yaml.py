import copy

import osdt
import yaml


from osdt_examples.models import ball,sensor



if __name__ == "__main__":
    #osdt.constructor.create_environment_opfile(systems={"ball":ball.opfile,"pos_sensor":sensor.opfile,"vel_sensor":sensor.opfile},connections=8,integrator=True,run=True,path="test10.yaml")
    osdt.constructor.build_figure_file(layout=[[1],[2]],args={"pos_system":[],"vel_system":[]},path="fig11")