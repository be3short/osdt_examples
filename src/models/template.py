# model template
# arguments: x = state, system = dynamical system, x_dot = state derivative,
# x_plus = post-jump state, *args = non-keyword args, **argmap = keyword args
import osdt as dt


class State(dt.Object):  # state object
    def __init__(self, value_1=0.0):
        self.value1 = value_1


class Params(dt.Object):  # parameters object
    def __init__(self, parameter_1=1.0):
        self.parameter_1 = parameter_1


class Connections(dt.Object):  # function object
    def __init__(self, connection_1=None):
        self.connection_1 = connection_1


def C(x, s):  # flow set (state in continuous domain)
    return x.value1 >= 0.0


def F(x, x_dot, s):  # flow map (continuous dynamics)
    x_dot.value1 = -1.0


def D(x, s):  # jump set (state in discrete domain)
    return x.value1 <= 0.0


def G(x, x_plus, s):  # jump map (discrete dynamics)
    x_plus.value1 = 0.0


def U(x, s, *args, **argmap):  # input map (determine input)
    return None


def Y(x, s, *args, **argmap):  # output map (determine output)
    return None


def initialize(s): # initialize function
    pass


def routine(s): # routine function
    pass

