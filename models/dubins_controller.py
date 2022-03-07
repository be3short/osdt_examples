import math
import osdt


VEHICLE = "VEHICLE"


class State:
    def __init__(self, turn=1.0, velocity=0.0):
        self.turn = turn
        self.velocity = velocity

class VehicleInput:
    def __init__(self,x_position=0.0, y_position=0.0, orientation=0.0):
        self.x_position = x_position
        self.y_position = y_position
        self.orientation = orientation

def C(x, system): # flow set (state in continuous domain)
    return True


def F(x, x_dot, system): # flow map (continuous dynamics)
    pass


def D(x, system): # jump set (state in discrete domain)
    u = system.get_input()
    jump = u.x_position >= 1 and x.turn == 2 or u.x_position <= -1 and x.turn == 1
    return jump


def G(x, x_plus, system): # jump map (discrete dynamics)
    u = system.get_input()
    if u.x_position >= 1 and x.turn == 2 or u.x_position <= -1 and x.turn == 1:
        x_plus.turn = 3 - x.turn

'''
def U(x, system,*args, **argmap): # input map (determine input)
    """Input map where dubins controller is expecting to get a VehicleInput object from the vehicle"""
    vehicle = system.get(VEHICLE)
    vehicle_output = vehicle.get_output(system)
    return vehicle_output
'''

def U(x, system,*args, **argmap): # input map (determine input)
    """Input map where dubins controller is getting dubins_vehicle.State and construct the VehicleInput object"""
    vehicle = system.get(VEHICLE)
    output = vehicle.get_output()
    if type(output) is dict:
        u = VehicleInput(x_position=output["x_position"],
                         y_position=output["y_position"],
                         orientation=output["orientation"])
    else:
        vehicle_state:dubins_vehicle.State = vehicle.get_output()
        u = VehicleInput(x_position=vehicle_state.x_position,y_position=vehicle_state.y_position,
                     orientation=vehicle_state.orientation)
    return u

def Y(x, system,*args, **argmap): # output map (determine output)
    return x

def Y_convert(x, system,*args, **argmap):  # output map (determine output)
    y = dubins_vehicle.ControlInput(x.turn, x.velocity)
    return y


def createz(x,**model): # create a new system
    return osdt.create_system(x=x,**model)


def create(state=State(),vars=None,c=C,f=F,d=D,g=G,u=U,y=Y,initialize=None,routine=None,id="dubins_control"): # create a new system
    return osdt.create_system(x=state,vars=vars,c=c,f=f,d=d,g=g,u=u,y=y,initialize=initialize,routine=routine,id=id)
