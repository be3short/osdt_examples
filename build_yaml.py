import copy

import osdt
import yaml


from osdt_examples.models import ball,sensor



if __name__ == "__main__":
    #
    osdt.constructor.build_figure_file(layout=[[1],[2]],args={"pos_system":[],"vel_system":[]},path="fig12")
    osdt.constructor.create_environment_opfile(
        systems={"ball": ball.opfile, "pos_sensor": sensor.opfile,
                 "vel_sensor": sensor.opfile}, connections=2, integrator=True,
        run=True,opfile_calls={"fig":"osdt_examples/fig10.yaml"}, path="test13")