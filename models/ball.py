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
    x_dot.y_velocity = -system.get(Params).gravity

def D(x, system): # jump set (discrete domain)
    return x.y_position <= 0.0 and x.y_velocity < 0.0

def G(x, x_plus, system): # jump map (discrete dynamics)
    x_plus.y_position = 0.0  # x.y_position
    x_plus.y_velocity = -system.get(Params).restitution*x.y_velocity

def U(x, system, *args, **argmap): # input map (determine input)
    return None

def Y(x, system, *args, **argmap): # output map (determine output)
    return x

def Y_dict(x, hs, *args, **argmap): # output map (determine output)
    return x.__dict__

def initialize(systemtem): # initialize the systemtem when the environment starts
    pass

def create(x:State,p:Params,**model): # create a new system
    return osdt.create_system(x=x,vars={PARAMS: p},**model)

opfile = osdt.create_system_opfile(__name__,State(), p={Params: Params()})


