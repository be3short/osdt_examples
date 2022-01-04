# model template
# arguments: x = state, system = dynamical system, x_dot = state derivative,
# x_plus = post-jump state, *args = non-keyword args, **argmap = keyword args
import osdt

class State: # state object
    def __init__(self, value=0.0):
        self.value = value

class Params: # parameters object
    def __init__(self, interval=1.0):
        self.interval = interval

class Params2:
    def __init__(self,params1=None,params2=Params()):
        self.value=params1 if params1 is not None else Params()
        self.params2=params2 if params2 is not None else Params()

def C(x, system): # flow set (state in continuous domain)
    return x.value >= 0.0

def F(x, x_dot, system): # flow map (continuous dynamics)
    x_dot.value = -1.0

def D(x, system): # jump set (state in discrete domain)
    return x.value <= 0.0

def G(x, x_plus, system): # jump map (discrete dynamics)
    osdt.get_logger().info(system.get(None))
    x_plus.value = system.get(Params).interval

def U(x, system, *args, **argmap): # input map (determine input)
    return None

def Y(x, system, *args, **argmap): # output map (determine output)
    return None

def initialize(system): # initialize the system when the environment starts
    pass

def create(x,p,**model): # create a new system
    return osdt.create_system(x=x,vars={Params: p},**model)


