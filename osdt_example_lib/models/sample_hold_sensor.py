"""Bouncing ball model"""
import osdt
import copy

INPUT = "INPUT"
PARAMS="PARAMS"

class State(): # state class
    def __init__(self, value=0.0, timer=0.0):
        self.value = value
        self.timer = timer

class Params: # parameters class
    def __init__(self, sample_period=1.0, sample_field=""):
        self.sample_period = sample_period
        self.sample_field = sample_field

def C(x, hs): # flow set (continuous domain)
    return x.timer >= 0.0

def F(x, x_dot, hs): # flow map (continuous dynamics)
    x_dot.timer = -1.0

def D(x, hs): # jump set (discrete domain)
    return x.timer <= 0.0

def G(x, x_plus, hs): # jump map (discrete dynamics)
    x_plus.value = hs.get_input()
    x_plus.timer = hs.get(PARAMS).sample_period

def U(x, hs, *args, **argmap): # input map (determine input value)
    signal_system = hs.get(INPUT)
    sample_field = hs.get(PARAMS).sample_field
    signal_value = signal_system.get_output()[sample_field]
    return signal_value

def Y(x, hs, *args, **argmap): # output map (determine output value)
    return x.value

def connect_input(sh_system,input_system):
    osdt.get_system(sh_system).set(INPUT,osdt.get_system(input_system))

def create(x_vals={},p_vals={},**model):
    state = State(**x_vals)
    params = Params(**p_vals)
    system = osdt.create_system(x=state,vars={PARAMS: params},**model)
    return system