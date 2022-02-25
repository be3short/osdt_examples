"""Bouncing ball model"""
import osdt
import math

class State():  # state
    def __init__(self, angle=1.0,velocity=0.0):
        self.angle = angle
        self.velocity = velocity

class Params():  # parameters
    def __init__(self, length=1.0, mass=1.0, gravity =9.81):
        self.length = length
        self.mass = mass
        self.gravity = gravity


def F(x, x_dot, hs):
    x_dot.angle = x.velocity
    x.acceleration = -(hs.get(Params).gravity/hs.get(Params).length)*math.sin(x.angle)
    x_dot.velocity = x.acceleration

def C(x,hs):
    return True


if __name__ == "__main__":

    system = osdt.create_system(State(angle=1.5, velocity=0.0),f=F, vars={Params:Params(length=1.0, mass=1.0, gravity=9.81)})

    # run the simulation
    osdt.run(t=10.0, j=20)

    # create a figure
    fig = osdt.create_figure(layout=[[1],[2]],
                                 title="Pendulum",
                                 width=1600, height=600)

    # plot the angle and velocity
    fig.sub(1).plot("angle")
    fig.sub(2).plot("velocity")

    # display all figures
    osdt.display()




