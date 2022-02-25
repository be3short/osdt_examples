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
    outside_temp = hs.get(Params).outside_temperature
    x_dot.temperature = (-x.temperature + hs.get(Params).heater_capacity * thermostat_on + outside_temp);


def D(x, hs):
    return False


def G(x, x_plus, hs):
    pass


def U(x, hs, *args, **argmap):
    thermostat_controller = hs.get(CONTROLLER)
    control_signal = thermostat_controller.get_output()
    return control_signal


def Y(x, hs, *args, **argmap):
    return hs.x().temperature


class TemperatureSystem(dt.System):
    def __init__(self, x=State, c=C, f=F, d=D, g=G, u=U, y=Y, p=Params(), id="temperature_sys"):
        super().__init__(x=x, c=c, f=f, d=d, g=g, u=u, y=y, id=id, vars={Params:p})

def create(c=C, f=F, d=D, g=G, u=U, y=Y, id="temperature_sys",
                initial_temp=60.0, heater_capacity=90.0, outside_temp=40.0):
        state=State(temperature=initial_temp)
        params=Params(heater_capacity=heater_capacity,
                      outside_temperature=outside_temp)
        return TemperatureSystem(x=state, c=c, f=f, d=d, g=g, u=u, y=y, id=id,p=params)


def create(c=C, f=F, d=D, g=G, u=U, y=Y, id="temperature_sys",
                initial_temp=60.0, heater_capacity=90.0, outside_temp=40.0):
        state=State(temperature=initial_temp)
        params=Params(heater_capacity=heater_capacity,
                      outside_temperature=outside_temp)
        return TemperatureSystem(x=state, c=c, f=f, d=d, g=g, u=u, y=y, id=id,p=params)