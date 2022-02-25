"""Bouncing ball model"""
import osdt as dt
import math,figure

class State():  # state
    def __init__(self, angle=1.0,velocity=0.0):
        self.angle = angle
        self.velocity = velocity

def get_pendulum_output(x:State, hs):
    return x.angle

class Params():  # parameters
    def __init__(self, length=1.0, mass=1.0, gravity =9.81):
        self.length = length
        self.mass = mass
        self.gravity = gravity


def F(x, x_dot, hs):
    x_dot.angle = x.velocity
    x.acceleration = -(hs.params.gravity/hs.params.length)*math.sin(x.angle)
    x_dot.velocity = x.acceleration


def Y(x, hs, **args):
    if system in args:
        func = hs.outs[system]
    return func(x,hs)

# create the pendulum system
system = dt.create_system(State(angle=1.5, velocity=0.0), f=F,
                          params=Params(length=1.0, mass=1.0, gravity=9.81))

system2 =  dt.create_system(State(angle=1.5, velocity=0.0), f=F,
                          params=Params(length=1.0, mass=1.0, gravity=9.81))
outputs = {system2:get_pendulum_output}
system2.outs = outputs




# run the simulation
dt.run(t=10.0, j=20)

# create a figure
fig = figure.MultiPlotFigure(layout=[[1],[2]],
                             title="Pendulum",
                             width=1600, height=600)

# plot the angle and velocity
fig.sub(1).plot("angle")
fig.sub(2).plot("velocity")

# display all figures
dt.display()




