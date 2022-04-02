import sys
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
    def __init__(self, sample_period=0.25, sample_field=""):
        self.sample_period = sample_period
        self.sample_field = sample_field


class StateMulti(): # state class
    def __init__(self, timer=0.0, values=[]):
        self.timer = timer
        for val_name in values:
            self.__dict__[val_name]=0.0

class ParamsMulti: # parameters class
    def __init__(self, sample_period=1.0, sample_fields=[]):
        self.sample_period = sample_period
        self.sample_fields = sample_fields

def C(x, system): # flow set (continuous domain)
    return x.timer >= 0.0

def F(x, x_dot, system): # flow map (continuous dynamics)
    x_dot.timer = -1.0

def D(x, system): # jump set (discrete domain)
    return x.timer <= 0.0

def G(x, x_plus, system): # jump map (discrete dynamics)
    x_plus.value = system.get_input()
    x_plus.timer = system.get(Params).sample_period


def G_multi(x, x_plus, system): # jump map (discrete dynamics)
    signal_input = system.get_input()
    for signal in signal_input:
        signal_value = signal_input[signal]
        x_plus.__dict__[signal]=signal_value
    x_plus.timer = system.get(Params).sample_period

def U(x, system, *args, **argmap): # input map (determine input value)
    signal_system = system.get(INPUT)
    sample_field = system.get(Params).sample_field
    signal_input = signal_system.get_output()
    if len(sample_field)==0:
        return signal_input
    else:
        if type(signal_input) is not dict: signal_input = signal_input.__dict__
        signal_value = signal_input[sample_field]
    return signal_value

def U_multi(x, system, *args, **argmap): # input map (determine input value)
    signal_system = system.get(Params)
    signal_input = signal_system.get_output()
    if type(signal_input) is not dict: signal_input = signal_input.__dict__
    signal_values = {}
    for sample_field in system.get(Params).sample_fields:
        signal_values[sample_field] = signal_input[sample_field]
    return signal_values

def Y_multi(x, system, *args, **argmap): # output map (determine output value)
    return x.__dict__

def Y(x, system, *args, **argmap): # output map (determine output value)
    return x.value

def initialize(system): # initialize the system when the environment starts
    pass

def connect_input(sensor_system, input_system):
    osdt.get_system(sensor_system).set(INPUT,osdt.get_system(input_system))

def create(state=State(),params=Params(),c=C,f=F,d=D,g=G,u=U,y=Y,initialize=None,routine=None,id="sensor",input_sys=None): # create a new system
    system=osdt.create_system(x=state,vars={Params: params},c=c,f=f,d=d,g=g,u=u,y=y,initialize=initialize,routine=routine,id=id)
    if input_sys is not None:
        system.set(INPUT,input_sys)
    return system