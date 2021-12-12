import math
import osdt
from osdt_example.models import dubins_vehicle

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

def C(x, system):
    return False


def F(x, x_dot, system):
    pass


def D(x, system):
    u = system.get_input()
    jump = u.x_position >= 1 and x.turn == 2 or u.x_position <= -1 and x.turn == 1
    return jump


def G(x, x_plus, system):
    u = system.get_input()
    if u.x_position >= 1 and x.turn == 2 or u.x_position <= -1 and x.turn == 1:
        x_plus.turn = 3 - x.turn


def U(x, system,*args, **argmap):
    """Input map where dubins controller is expecting to get a VehicleInput object from the vehicle"""
    vehicle = system.get(VEHICLE)
    vehicle_output = vehicle.get_output(system)
    return vehicle_output


def U_convert(x, system,*args, **argmap):
    """Input map where dubins controller is getting dubins_vehicle.State and construct the VehicleInput object"""
    vehicle = system.get(VEHICLE)
    vehicle_state:dubins_vehicle.State = vehicle.get_output(system)
    u = VehicleInput(x_position=vehicle_state.x_position,y_position=vehicle_state.y_position,
                     orientation=vehicle_state.orientation)
    return u

def Y(x, system,*args, **argmap):
    return x

def Y_convert(x, system,*args, **argmap):
    y = dubins_vehicle.ControlInput(x.turn, x.velocity)
    return y


def create(x,**model):
    return osdt.create_system(x=x,**model)

