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

def C(x, sys): # flow set (continuous domain)
    return x.y_position >= 0.0

def F(x, x_dot, sys): # flow map (continuous dynamics)
    x_dot.y_position = x.y_velocity
    x_dot.y_velocity = -sys.get(PARAMS).gravity

def D(x, sys): # jump set (discrete domain)
    return x.y_position <= 0.0 and x.y_velocity < 0.0

def G(x, x_plus, sys): # jump map (discrete dynamics)
    x_plus.y_position = 0.0  # x.y_position
    x_plus.y_velocity = -sys.get(PARAMS).restitution*x.y_velocity

def U(x, sys, *args, **argmap): # input map (determine input)
    return None

def Y(x, sys, *args, **argmap): # output map (determine output)
    return x

def Y_dict(x, hs, *args, **argmap): # output map (determine output)
    return x.__dict__

def initialize(system): # initialize the system when the environment starts
    pass

def create(x,p,**model):
    return osdt.create_system(x=x,vars={PARAMS: p},**model)



