import sys, os

import osdt
from osdt_examples.models import point_mass
"""
osdt run D:\osdt_dev\osdt_home\osdt_examples\applications\point_mass\point_mass.py -top_right_vel 0.5 -top_left_vel 0.5 -bottom_right_vel 0.5 -bottom_left_vel 0.5 -center_mass 50000000000000.0

"""
def defaults():
    osdt.set_configuration(time=100000.0,jumps=10)
    osdt.set_integrator(osdt.get_configuration().integrator_type, max_step=500.0)

def main(top_right_distance = 1000.0,
         top_left_distance = 1000.0,
         bottom_right_distance = 1000.0,
         bottom_left_distance = 1000.0,
         top_right_vel = 0.1,
         top_left_vel = 0.1,
         bottom_right_vel = 0.1,
         bottom_left_vel = 0.1,
         corner_mass = 100000000000.0,
         center_mass = 900000000000.0
         ):
    V_0=.1
    top_right = point_mass.create(x_position=top_right_distance, y_position=top_right_distance, x_velocity=-top_right_vel, y_velocity =top_right_vel, mass=corner_mass, id="top_right")
    top_left = point_mass.create(x_position=-top_left_distance, y_position=top_left_distance, x_velocity=-top_left_vel, y_velocity = -top_left_vel, mass=corner_mass, id="top_left")
    bottom_right = point_mass.create(x_position=bottom_right_distance, y_position=-bottom_right_distance, x_velocity=bottom_right_vel, y_velocity = bottom_right_vel, mass=corner_mass, id="bottom_right")
    bottom_left = point_mass.create(x_position=-bottom_left_distance, y_position=-bottom_left_distance, x_velocity=bottom_left_vel, y_velocity = -bottom_left_vel, mass=corner_mass, id="bottom_left")
    center_mass = point_mass.create(x_position=0.1, y_position=0.1, x_velocity=0.0, y_velocity = 0.0, mass=center_mass, id = "center")

    point_mass.connect_all_masses()
    osdt.run()
    xyfig = osdt.create_figure(width=1200, height=800, layout=[[1]], title="Point Mass Interaction",dpi=100 )
    xyfig.plot(1,x="x_position",y="y_position",max_points=1000)
    xyfig.export("xy_figure",format="png")
    #xyfig.plot(1,"y_position")

    osdt.display()
