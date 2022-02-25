import sys, os

import osdt
from osdt_examples.models import point_mass
from osdt_examples.models import point_mass as pm
import osdt
V_0=.1
state1 = pm.State(x_position=1000.0, y_position=1000.0, x_velocity=-V_0, y_velocity = V_0)
params1 = pm.Params(mass=1100020100.0)
system1 = osdt.create_system(x=state1, c=pm.C, f=pm.F, u=pm.U, vars={pm.PARAMS: params1}, id="small mass 1")


state2 = pm.State(x_position=-1000.0, y_position=-1000.0, x_velocity=V_0, y_velocity = -V_0)
params2 = pm.Params(mass=1100020110.0)
system2 = osdt.create_system(x=state2, c=pm.C, f=pm.F, u=pm.U, vars={pm.PARAMS: params2}, id="small mass 2")


state3 = pm.State(x_position=1000.0, y_position=-1000.0, x_velocity=V_0, y_velocity = V_0)
params3 = pm.Params(mass=1100020100.0)
system3 = osdt.create_system(x=state3, c=pm.C, f=pm.F, u=pm.U, vars={pm.PARAMS: params3}, id="small mass 3")

state4 = pm.State(x_position=-1000.0, y_position=1000.0, x_velocity=-V_0, y_velocity = -V_0)
params4 = pm.Params(mass=1100020100.0)
system4 = osdt.create_system(x=state4, c=pm.C, f=pm.F, u=pm.U, vars={pm.PARAMS: params4}, id="small mass 4")

state0 = pm.State(x_position=0.1, y_position=0.1, x_velocity=0.0, y_velocity = 0.0)
params0 = pm.Params(mass=911000220100.0)
system0 = osdt.create_system(x=state0, c=pm.C, f=pm.F, u=pm.U, vars={pm.PARAMS: params0}, id="large mass")

pm.connect_all_masses()
osdt.set_integrator(osdt.get_configuration().integrator_type, max_step=100.0)
#osdt.run(time=100000.0, jumps=20)
xyfig = osdt.create_figure(width=800, height=600, layout=[[1]], title="Point Mass Interaction",dpi=130)
xyfig.plot(1,x="x_position",y="y_position")
#xyfig.plot(1,"y_position")

osdt.display()

def create_opfile():
    fb = osdt.get_opfile_builder()
    for index in range(0,10):
        fb.add_sys("point_mass_"+str(index),point_mass,point_mass.State(x_position=osdt.random(100,1000),y_position=osdt.random(100,1000)),PARAMS=point_mass.Params)
    fb.add_func(None,point_mass.connect_all_masses)
    fb.add_func(None,osdt.run)
    fb.add_fig("figure",layout=[[1,2,3,3],[4,5,3,3]])
    fb.create_opfile("applications/python/pointmass.yaml")
create_opfile()
'''
# create a figure
fig = osdt.create_figure(layout=[[1,3,4,4], [2,3,4,4]],width=1200, height=600,
                         title="Bouncing Ball",dpi=130)
fig.configure_subplot(1, )
fig.subplot(1).plot("y_position", max_points=200)
fig.subplot(2).plot("y_velocity", max_points=200)
fig.subplot(3).plot(["y_position", "y_velocity"], max_points=200)
fig.subplot(4).plot(x="y_velocity", y="y_position", max_points=200)

# create a figure
fig2 = osdt.create_figure(width=800, height=600, layout=[[1],[2]], title="Bouncing Ball",dpi=130)
fig2.configure_subplot(1, x_axis="Time (s)", y_axis="Position (m)")
fig2.configure_subplot(2, x_axis="Time (s)", y_axis="Velocity (m/s)")
fig2.plot(1,"y_position")
fig2.plot(2,"y_velocity")
osdt.display()
'''



