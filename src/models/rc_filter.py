# rc_filter

# from https://en.wikipedia.org/wiki/Low-pass_filter
# d(v_out)/dt = (v_in - v_out)/RC

# arguments: x = state, system = dynamical system, x_dot = state derivative,
# x_plus = post-jump state, *args = non-keyword args, **argmap = keyword args

PARAMS="RC_FILTER_PARAMS"


class State: # state object
    def __init__(self, v_in=0.0,v_out=0.0):
        self.v_in = v_in
        self.v_out = v_out


class Params: # parameters object
    def __init__(self, resistor=1500.0,capacitor=10.0e-6):
        self.resistor=resistor
        self.capacitor=capacitor

def C(x, system): # flow set (state in continuous domain)
    return True

def F(x, x_dot, system): # flow map (continuous dynamics)
    x_dot.v_in=0.0
    params = system.get(PARAMS)
    x_dot.v_out=(x.v_in-x.v_out)/(params.resistor*params.capacitor)

def U(x, system, *args, **argmap): # input map (determine input)
    return None

def Y(x, system, *args, **argmap): # output map (determine output)
    return None
