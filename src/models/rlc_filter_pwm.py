# rc_filter

# from https://en.wikipedia.org/wiki/Low-pass_filter
# i(t) = ( v(t) - (L*di_dt) ) / (R+1/C)

# arguments: x = state, system = dynamical system, x_dot = state derivative,
# x_plus = post-jump state, *args = non-keyword args, **argmap = keyword args

PARAMS="RC_FILTER_PARAMS"


class State: # state object
    def __init__(self,params, v_in=0.0,v_out=0.0):
        self.vc=0.0
        self.vl =0.0
        self.vr = 0.0#v_in
        self.i = v_in / params.resistor
        self.di_dt = 0.0
        self.toggle_timer = 0.0
        self.v_in=0.0

class Params: # parameters object
    def __init__(self, resistor=63.24,capacitor=100.0e-6,inductor=100e-3,max_voltage=3.3,frequency=10000.0,duty_cycle=.3):
        self.resistor=resistor
        self.capacitor=capacitor
        self.inductor=inductor
        self.max_voltage=max_voltage
        self.frequency=frequency
        self.duty_cycle=duty_cycle

def C(x, system): # flow set (state in continuous domain)
    return True

def F(x, x_dot, system): # flow map (continuous dynamics)
    params = system.get(PARAMS)
    x_dot.i=x.di_dt
    x_dot.vr=x.i*params.resistor
    x_dot.vl=x.di_dt*params.inductor
    x_dot.di_dt = - (params.resistor/params.inductor)*x.di_dt - (1/(params.inductor*params.capacitor))*x.i
    x_dot.vc =  x.i/params.capacitor
    x_dot.toggle_timer = -1.0
    x#_dot.v_out=(x.v_in-x.v_out)/(params.resistor*params.capacitor)

def D(x, system): # jump set (state in discrete domain)
    return x.toggle_timer <= 0.0

def G(x, x_plus, system): # jump map (discrete dynamics)
    params = system.get(PARAMS)
    cycle_length = 1/params.frequency
    if  x.v_in > 0:
        toggle_length = (1-params.duty_cycle) * cycle_length
    else:
        toggle_length = params.duty_cycle*cycle_length
    x_plus.v_in = 0.0 if x.v_in > 0 else params.max_voltage
    x_plus.i = (x_plus.v_in-x.di_dt) / (params.resistor+(1/params.capacitor))
    x_plus.toggle_timer = toggle_length

def U(x, system, *args, **argmap): # input map (determine input)
    return None

def Y(x, system, *args, **argmap): # output map (determine output)
    return None
