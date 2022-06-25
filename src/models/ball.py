"""Bouncing ball model"""
from random import random

import osdt


class State(osdt.Object): # state class
    def __init__(self, y_position=1.0, y_velocity=0.0):
        self.y_position = y_position
        self.y_velocity = y_velocity

class Params(osdt.Object): # parameters class
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

def new(state=State(), params=Params(), f= F, c=C, d=D, g=G, y= Y_dict, **fields):
    ball_sys=osdt.create_sys(x=state,c=c, f=f, g=g, d=d, y=y, id="ball", params=params, **fields)
    return ball_sys

def plot() -> osdt.Figure:
    fig = osdt.create_fig(layout=[[1], [2]], title="Pendulum", w=1600, h=600)
    # plot the angle and velocity
    fig.plot(1, "y_position")
   # fig.plot(1, "value")

    fig.plot(2, "y_velocity")
    return fig

def create(x=State(), p=Params(), c=C, f=F, d=D, g=G, u=U, y=Y_dict, id="ball", **args): # create a new system
    return osdt.create_sys(x=x, c=c, f=f, d=d, g=g, u=u, y=y, params=p, id=id, **args)


def create_multi(num_balls=1,
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
                              y= Y_dict,id="ball", **fields):
    for ind in range(0,num_balls):
        y_position=osdt.random(y_position_min,y_position_max)
        y_velocity=osdt.random(y_velocity_min,y_velocity_max)
        ball_sys=osdt.create_sys(x=State(y_position, y_velocity), c=c, f=f, g=g, d=d, y=y, params=Params(gravity, restitution), id=id, **fields)
    return ball_sys


class BallSys(osdt.System):
    def __init__(self, params=None):
        super().__init__(state=State(1.0 + random() * 5.0), params=params if params is not None else Params(), c=C, f=F, d=D, g=G, u=U, y=Y_dict, id="ball")
        #osdt.add_systems(self)