# rc_filter

# from https://en.wikipedia.org/wiki/Low-pass_filter
# d(v_out)/dt = (v_in - v_out)/RC


# arguments: x = state, system = dynamical system, x_dot = state derivative,
# x_plus = post-jump state, *args = non-keyword args, **argmap = keyword args
import osdt
PARAMS="RC_FILTER_PWM_PARAMS"


class State: # state object
    def __init__(self, v_in=0.0,v_out=0.0,toggle_timer=0.0):
        self.v_in = v_in
        self.v_out = v_out
        self.toggle_timer = toggle_timer


class Params: # parameters object
    def __init__(self, resistor=1500.0,capacitor=10.0e-6,max_voltage=3.3,frequency=10000.0,duty_cycle=.3):
        self.resistor=resistor
        self.capacitor=capacitor
        self.max_voltage=max_voltage
        self.frequency=frequency
        self.duty_cycle=duty_cycle

def C(x, system): # flow set (state in continuous domain)
    return True

def F(x, x_dot, system): # flow map (continuous dynamics)
    x_dot.v_in=0.0
    params = system.get(PARAMS)
    x_dot.v_out=(x.v_in-x.v_out)/(params.resistor*params.capacitor)
    x_dot.toggle_timer = -1.0

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
    x_plus.toggle_timer = toggle_length


def U(x, system, *args, **argmap): # input map (determine input)
    return None

def Y(x, system, *args, **argmap): # output map (determine output)
    return None



def create(x_vals={},p_vals={},**model):
    state = State(**x_vals)
    params = Params(**p_vals)
    system = osdt.create_system(x=state,vars={PARAMS: params},**model)
    return system

