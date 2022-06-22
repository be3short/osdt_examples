import osdt
import osdt as dt

TEMPERATURE = "TEMPERATURE"
OUTSIDE_TEMPERATURE = "OUTSIDE_TEMPERATURE"
THERMOSTAT_ON = "THERMOSTAT_ON"
CONTROLLER = "CONTROLLER"
PARAMS = "PARAMS"

class State:
    def __init__(self, temperature=60.0):
        self.temperature = temperature


class Params:
    def __init__(self, heater_capacity=90.0, outside_temperature=40.0):
        self.heater_capacity = heater_capacity
        self.outside_temperature = outside_temperature


def C(x, hs):
    return True


def F(x, x_dot, hs):
    thermostat_on = hs.get_input()
    outside_temp = hs.params.outside_temperature
    x_dot.temperature = (-x.temperature + hs.params.heater_capacity * thermostat_on + outside_temp);


def D(x, hs):
    return False


def G(x, x_plus, hs):
    pass


def U(x, hs, *args, **argmap):
    thermostat_controller = hs.get(CONTROLLER)
    control_signal = thermostat_controller.get_output()
    return control_signal


def Y(x, hs, *args, **argmap):
    return  x.temperature


def create2(initial_temp=60.0, heater_capacity=90.0, outside_temp=40.0, id="temperature") -> osdt.System:
    temperature_state = State(temperature=initial_temp)
    temperature_params = Params(heater_capacity=heater_capacity,
                    outside_temperature=outside_temp)
    temperature = osdt.create_sys(x=temperature_state, c=C, f=F, d=D, g=G, u=U, y=Y, id=id,
                             vars={Params:temperature_params} )
    return temperature

def connect_controller(temperature_system, controller_system):
    temperature_system.set(CONTROLLER,controller_system)


def create(state=State(),params=Params(),c=C,f=F,d=None,g=None,u=U,y=Y,initialize=None,routine=None,id="heater_system"): # create a new system
    return osdt.create_sys(x=state,params=params,c=c,f=f,d=d,g=g,u=u,y=y,initialize=initialize,routine=routine,id=id)


