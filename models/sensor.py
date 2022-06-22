import inspect
import sys
"""Bouncing ball model"""
import osdt
import copy

INPUT = "input_sys"
PARAMS="PARAMS"

class State(): # state class
    def __init__(self, value=0.0, timer=0.0):
        self.value = value
        self.timer = timer

class Params(): # parameters class
    def __init__(self, sample_period=0.1, sample_field=""):
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

class Connector(osdt.ObjectBase):
    def __init__(self):# input_conn=None):
        super().__init__()


    def connect(self,input_sys):
        self.get_parent().input_sys=input_sys

    def get_input(self):
        return self.get_parent().input_sys

def C(x, system): # flow set (continuous domain)
    return x.timer >= 0.0

def F(x, x_dot, system): # flow map (continuous dynamics)
    x_dot.timer = -1.0

def D(x, system): # jump set (discrete domain)
    return x.timer <= 0.0

def G(x, x_plus, system): # jump map (discrete dynamics)
    x_plus.value = system.u()
    x_plus.timer = system.params.sample_period


def G_multi(x, x_plus, system): # jump map (discrete dynamics)
    signal_input = system.conn.get_input_sys()
    for signal in signal_input:
        signal_value = signal_input[signal]
        x_plus.__dict__[signal]=signal_value
    x_plus.timer = system.get(Params).sample_period

def U(x, system, *args, **argmap): # input map (determine input value)
    signal_system = system.conn.get_input()
    sample_field = system.params.sample_field
    signal_input = signal_system.y()
    if len(sample_field)==0:
        return signal_input
    else:
        if type(signal_input) is not dict: signal_input = signal_input.__dict__
        signal_value = signal_input[sample_field]
    return signal_value

def U_multi(x, system, *args, **argmap): # input map (determine input value)
    signal_system = system.params
    signal_input = signal_system.y()
    if type(signal_input) is not dict: signal_input = signal_input.__dict__
    signal_values = {}
    for sample_field in system.params.sample_fields:
        signal_values[sample_field] = signal_input[sample_field]
    return signal_values

def Y_multi(x, system, *args, **argmap): # output map (determine output value)
    return x.__dict__

def Y(x, system, *args, **argmap): # output map (determine output value)
    return x.value

def initialize(system): # initialize the system when the environment starts
    pass

def create(state=State(),params=None,c=C,f=F,d=D,g=G,u=U,y=Y ,id="sensor",input_sys=None,add=True): # create a new system
    system=osdt.create_sys(x=state,c=c,f=f,d=d,g=g,u=u,y=y,id=id,
                           params=Params() if params is None else params,
                           conn=Connector(),add=add)

    return system

class SHSensor(osdt.System):
    def __init__(self, x=State(), f=F, c=C, d=D, g=G, y=Y, p=Params,
           id="sh_sensor", label="Sample & Hold Sensor", **objs):

        super().__init__(x=x, c=c, f=f, g=g, d=d, y=y,
                               id=id, label=label, **objs)

        self.p=p
        self.connected_sys=None

    def get_connected(self):
        return self.connected_sys
'''
class SensorSystem(osdt.System):
    def __init__(self,state=State(),params=Params(),c=C,f=F,d=D,g=G,u=U,y=Y,initialize=None,routine=None,id="sensor",input_sys=None):
        super().__init__(x=state,c=c,f=f,d=d,g=g,u=u,y=y,initialize=initialize,routine=routine,id=id,params=params)
        self.set(INPUT,None)
    def connect(self,input):
        self.set(INPUT,input)


'''