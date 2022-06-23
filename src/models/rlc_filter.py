# rc_filter

# from https://en.wikipedia.org/wiki/Low-pass_filter
# d(v_out)/dt = (v_in - v_out)/RC

# arguments: x = state, system = dynamical system, x_dot = state derivative,
# x_plus = post-jump state, *args = non-keyword args, **argmap = keyword args

PARAMS="RC_FILTER_PARAMS"


class State: # state object
    def __init__(self,params, v_in=1.0,v_out=0.0):
        self.vc=0.0
        self.vl =0.0
        self.vr = v_in
        self.i = v_in / params.resistor
        self.di_dt = 0.0

class Params: # parameters object
    def __init__(self, resistor=63.24,capacitor=100.0e-6,inductor=100e-3):
        self.resistor=resistor
        self.capacitor=capacitor
        self.inductor=inductor

def C(x, system): # flow set (state in continuous domain)
    return True

def F(x, x_dot, system): # flow map (continuous dynamics)
    params = system.get(PARAMS)
    x_dot.i=x.di_dt
    x_dot.vr=x.i*params.resistor
    x_dot.vl=x.di_dt*params.inductor
    x_dot.di_dt = - (params.resistor/params.inductor)*x.di_dt - (1/(params.inductor*params.capacitor))*x.i
    x_dot.vc =  x.i/params.capacitor
    x#_dot.v_out=(x.v_in-x.v_out)/(params.resistor*params.capacitor)

def U(x, system, *args, **argmap): # input map (determine input)
    return None

def Y(x, system, *args, **argmap): # output map (determine output)
    return None
