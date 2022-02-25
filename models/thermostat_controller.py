import osdt as dt

TEMPERATURE = "TEMPERATURE"

class State:
    def __init__(self, thermostat_on=0.0, set_temperature=60.0):
        self.thermostat_on = thermostat_on
        self.set_temperature = set_temperature
        self.measured_temp = 0.0
        self._non_dynamic=[ "measured_temp"]


class Params:
    def __init__(self, hysteresis_range=5.0):
        self.hysteresis_range = hysteresis_range


def C(x, hs):
    return True


def F(x, x_dot, hs):
    x.measured_temp=hs.get_input()


def D(x, hs):
    current_temp = hs.get_input()
    if hs.get(Params).hysteresis_range + x.set_temperature < current_temp and x.thermostat_on > 0.0:
        return True
    elif x.set_temperature - hs.get(Params).hysteresis_range > current_temp and x.thermostat_on <= 0.0:
        return True
    return False


def G(x, x_plus, hs):
    current_temp = hs.get_input()
    if hs.get(Params).hysteresis_range + x.set_temperature < current_temp and x.thermostat_on > 0.0:
        x_plus.thermostat_on = 0.0
    elif x.set_temperature - hs.get(Params).hysteresis_range > current_temp and x.thermostat_on <= 0.0:
        x_plus.thermostat_on = 1.0


def U(x, hs, *args, **argmap):
    temperature_sys = hs.get(TEMPERATURE)
    temperature_value = temperature_sys.get_output()
    return temperature_value


def Y(x, hs, *args, **argmap):
    return x.thermostat_on

def connect_temperature_system(controller_sys, temperature_sys):
    controller_sys.set(TEMPERATURE,temperature_sys)

class ThermostatController(dt.System):
    def __init__(self, x=State, c=C, f=F, d=D, g=G, u=U, y=Y, p=Params(), id="thermostat_controller"):
        super().__init__(x=x, c=c, f=f, d=d, g=g, u=u, y=y, id=id, vars={Params:p})

def create(c=C, f=F, d=D, g=G, u=U, y=Y, id="thermostat_controller",
                thermostat_on=0.0, set_temperature=60.0, hysteresis_range=5.0):
        state=State(thermostat_on=thermostat_on, set_temperature=set_temperature)
        params=Params(hysteresis_range=hysteresis_range)
        return ThermostatController(x=state, c=c, f=f, d=d, g=g, u=u, y=y, id=id,p=params)