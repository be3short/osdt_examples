# model template
# arguments: x = state, system = dynamical system, x_dot = state derivative,
# x_plus = post-jump state, *args = non-keyword args, **argmap = keyword args

class State: # state object
    def __init__(self, value_1=0.0):
        self.value1 = value_1

class Params: # parameters object
    def __init__(self, parameter_1=1.0):
        self.parameter1 = parameter_1

def C(x, system): # flow set (state in continuous domain)
    return x.value1 >= 0.0

def F(x, x_dot, system): # flow map (continuous dynamics)
    x_dot.value1 = -1.0

def D(x, system): # jump set (state in discrete domain)
    return x.value1 <= 0.0

def G(x, x_plus, system): # jump map (discrete dynamics)
    x_plus.value1 = 1.0

def U(x, system, *args, **argmap): # input map (determine input)
    return None

def Y(x, system, *args, **argmap): # output map (determine output)
    return None

def initialize(system): # initialize the system when the environment starts
    pass
