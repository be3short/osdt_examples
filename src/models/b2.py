"""Bouncing ball model"""

import osdt
from osdt import PARAMS
CONNECTOR="Test"


class State(): # state class
    def __init__(self, y_position=1.0, y_velocity=0.0):
        self.y_position = y_position
        self.y_velocity = y_velocity

class Params(): # parameters class
    def __init__(self, gravity=9.81, restitution=0.9):
        self.gravity = gravity
        self.restitution = restitution

def C(x, system): # flow set (continuous domain)
    return x.y_position >= 0.0

def F(x, x_dot, system): # flow map (continuous dynamics)
    x_dot.y_position = x.y_velocity
    x_dot.y_velocity = -system.params.gravity

def D(x, system): # jump set (discrete domain)
    return x.y_position <= 0.0 and x.y_velocity < 0.0

def G(x, x_plus, system): # jump map (discrete dynamics)
    x_plus.y_position = 0.0  # x.y_position
    x_plus.y_velocity = -system.params.restitution * x.y_velocity

def U(x, system, *args, **argmap): # input map (determine input)
    return None

def Y(x, system, *args, **argmap): # output map (determine output)
    return x

def Y_dict(x, hs, *args, **argmap): # output map (determine output)
    return x.__dict__

def initialize(systemtem): # initialize the systemtem when the environment starts
    pass

def new(state=State(), params=Params(),f= F,c=C,d=D,g=G,y= Y_dict, **fields):
    ball_sys=osdt.create_sys(x=state,c=c, f=f, g=g, d=d, y=y, id="ball", params=params, **fields)
    return ball_sys
def create(num_balls=1,
                              y_position_min=1.0,
                              y_position_max=3.0,
                              y_velocity_min=0.0,
                              y_velocity_max=1.0,
                              gravity = 9.81,
                              restitution = .97,
                              f= F,
                              c= C,
                              d= D,
                              g= G,
                              y= Y_dict, **fields):
    for ind in range(0,num_balls):
        y_position=osdt.random(y_position_min,y_position_max)
        y_velocity=osdt.random(y_velocity_min,y_velocity_max)
        ball_sys=osdt.create_sys(State(y_position, y_velocity),
                                 c=c, f=f, g=g, d=d, y=y, params=Params(gravity,restitution), id="ball", **fields)
    return ball_sys

def create2(num_balls=1,
                              y_position_min=1.0,
                              y_position_max=3.0,
                              y_velocity_min=0.0,
                              y_velocity_max=1.0,
                              gravity = 9.81,
                              restitution = .97,
                              f= F,
                              c= C,
                              d= D,
                              g= G,
                              y= Y_dict, **fields):
    for ind in range(0,num_balls):
        y_position=osdt.random(y_position_min,y_position_max)
        y_velocity=osdt.random(y_velocity_min,y_velocity_max)
        ball_sys=osdt.const.SystemConstructor(State(y_position, y_velocity),
                                 c=c, f=f, g=g, d=d, y=y, vars={ Params:Params(gravity,restitution)}, id="ball", params=Params(gravity,restitution), **fields)
    return ball_sys


def plot():
    fig = osdt.create_fig(layout=[[1], [2]], title="Pendulum", w=1600, h=600)
    # plot the angle and velocity
    fig.plot(1, "y_position")
    fig.plot(2, "y_velocity")


def oldplot():
    fig = osdt.figure.create_fig()
    fig.plot(1,"y_position")
    osdt.figure.display()
def main():
    ballsys=create(3)

    osdt.run()
    oldplot()
    osdt.display()
    osdt.get_data().to_csv("bal.csv")
    print(osdt.dataset.DataHandler.handler.__dict__)
if __name__ == "__main__":
    main()