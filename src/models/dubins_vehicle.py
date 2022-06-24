import math
import osdt
from osdt_examples.models import dubins_controller

CONTROLLER = "CONTROLLER"
VEHICLE = "VEHICLE"

class State:
    def __init__(self, x_position=1.0, y_position=0.0, orientation=0.5):
        self.x_position = x_position
        self.y_position = y_position
        self.orientation = orientation


class ControlInput:
    def __init__(self, turn_state=0.0, velocity=0.5):
        self.turn_state = turn_state
        self.velocity = velocity


def C(x, system): # flow set (state in continuous domain)
    u = system.u()
    flow = x.x_position < 1 and u.turn_state == 2 or x.x_position > -1 and u.turn_state == 1
    return flow


def F(x, x_dot, system): # flow map (continuous dynamics)
    u = system.u()
    x_dot.x_position = u.velocity * math.cos(x.orientation)
    x_dot.y_position = u.velocity * math.sin(x.orientation)
    x_dot.orientation = - x.orientation + (3 * math.pi / 4 if u.turn_state == 1 else math.pi / 4 if u.turn_state == 2 else 0)


def D(x, system): # jump set (state in discrete domain)
    return False


def G(x, x_plus, system): # jump map (discrete dynamics)
    pass

'''
def U(x, system, *args, **argmap): # input map (determine input)
    """Input map where dubins vehicle is expecting to get a ControlInput object from the controller"""
    controller = system.get(CONTROLLER)
    u = controller.y()
    return u
'''

def U(x, system, *args, **argmap): # input map (determine input)
    """Input map where dubins controller is getting dubins_controller.State and constructs the ControlInput object"""
    controller = system.controller
    output = controller.y()
    if type(output) is dict:
        u = ControlInput(turn_state=output["turn"],
                         velocity=output["velocity"])
    else:
        controller_state:dubins_controller.State = controller.y()
        u = ControlInput(turn_state=controller_state.turn,
                     velocity=controller_state.velocity)
    return u

def Y(x, system, *args, **argmap): # output map (determine output)
    return x

def Y_convert(x, system, *args, **argmap): # output map (determine output)
    y=dubins_controller.VehicleInput(x_position=x.x_position,y_position=x.y_position,orientation=x.orientation)
    return y

def initialize(system): # initialize the system when the environment starts
    pass

def createz(x,**model): # create a new system
    return osdt.create_system(x=x,**model)

def create(state=State(),vars=None,c=C,f=F,d=D,g=G,u=U,y=Y,initialize=None,routine=None,id="dubins_vehicle"): # create a new system
    return osdt.create_system(x=state,vars=vars,c=c,f=f,d=d,g=g,u=u,y=y,initialize=initialize,routine=routine,id=id)
