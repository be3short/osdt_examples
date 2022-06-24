import osdt
import osdt as dt
from osdt_examples.models import heater_system

TEMPERATURE = "TEMPERATURE"

class State:
    no_model = ["measured_temp"]
    def __init__(self, thermostat_on=0.0, set_temperature=60.0):
        self.thermostat_on = thermostat_on
        self.set_temperature = set_temperature
        self.measured_temp = 0.0

class Params:
    def __init__(self, hysteresis_range=5.0):
        self.hysteresis_range = hysteresis_range
def C(x, hs):
    return True

def D(x, hs):
    current_temp = hs.u()
    if hs.params.hysteresis_range + x.set_temperature < current_temp and x.thermostat_on > 0.0:
        return True
    elif x.set_temperature - hs.params.hysteresis_range > current_temp and x.thermostat_on <= 0.0:
        return True
    return False


def G(x, x_plus, hs):
    current_temp = hs.u()
    if hs.params.hysteresis_range + x.set_temperature < current_temp and x.thermostat_on > 0.0:
        x_plus.thermostat_on = 0.0
    elif x.set_temperature - hs.params.hysteresis_range > current_temp and x.thermostat_on <= 0.0:
        x_plus.thermostat_on = 1.0


def U(x, hs, *args, **argmap):
    temperature_value = hs.heater.y()
    return temperature_value


def Y(x, hs, *args, **argmap):
    return x.thermostat_on

def pre(hs):
    hs.state.measured_temp=hs.u()


def create2(thermostat_on=0.0, set_temperature=60.0, hysteresis_range=15.0, temperature_system = None) -> osdt.System:
    controller_state = State(thermostat_on=thermostat_on, set_temperature=set_temperature)
    controller_params = Params(hysteresis_range=hysteresis_range)

    controller = osdt.create_sys(x=controller_state,
                                    d=D,
                                    g=G,
                                    u=U,
                                    y=Y,
                                    id="temperature",
                                    vars={
                                        Params: controller_params},
                                    routine=routine)

    return controller


def connect_heater(controller_sys, temperature_sys):
    controller_sys.set(TEMPERATURE,temperature_sys)



def create(state=State(),params=Params(),c=None,f=None,d=D,g=G,u=U,y=Y,initialize=None,routine=None,id="temperature_control"): # create a new system
    return osdt.create_sys(x=state,params= params,c=c,f=f,d=d,g=g,u=u,y=y,initialize=initialize,routine=routine,id=id)


def fig():
    # create a figure
    fig = dt.create_fig(layout=[[1], [2],[3]],
                           title="Thermostat Controlled Temperature",
                           w=1600, h=600)

    fig.plot(1,"temperature")
    fig.plot(2,"measured_temp")

    fig.plot(1,"value", system="temp_sensor")

    fig.plot(3,"thermostat_on")

    fig.plot(2,"value", system="controller_sensor")

  #  fig.export("figure1", format="png")
    osdt.display()

def main():
    osdt.clear()
    osdt.plotting.Figure2.clear_figures()
    cs=create()
    hs=heater_system.create()
    connect_heater(cs,hs)
    heater_system.connect_controller(hs,cs)
    osdt.run()
    fig()
if __name__ == "__main__":
    main()
