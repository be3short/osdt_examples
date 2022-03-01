import osdt
import osdt as dt

from osdt_examples.models import temperature_system,thermostat_controller,sensor
from random import random




def test(initial_temp=60.0 ):
    print(initial_temp)

def main_simple(initial_temp=60.0, heater_capacity=90.0, outside_temp=40.0,
        thermostat_on=0.0, set_temperature=60.0, hysteresis_range=15.0):
    temperature_state = temperature_system.State(temperature=initial_temp)
    temperature_params = temperature_system.Params(heater_capacity=heater_capacity,
                    outside_temperature=outside_temp)
    temperature = osdt.create_system(x=temperature_state, c=temperature_system.C, f=temperature_system.F, d=temperature_system.D, g=temperature_system.G, u=temperature_system.U, y=temperature_system.Y, id="temperature",
                             vars={temperature_system.Params:temperature_params} )

    controller_state = thermostat_controller.State(thermostat_on=thermostat_on, set_temperature=set_temperature)
    controller_params = thermostat_controller.Params(hysteresis_range=hysteresis_range)

    controller = osdt.create_system(x=controller_state, d=thermostat_controller.D, g=thermostat_controller.G, u=thermostat_controller.U, y=thermostat_controller.Y, id="temperature",
                             vars={thermostat_controller.Params:controller_params} , routine=thermostat_controller.routine )

    temperature.set(temperature_system.CONTROLLER,controller)
    controller.set(thermostat_controller.TEMPERATURE,temperature)

  #  dt.set_integrator(max_step=.01)
    dt.run()

    # create a figure
    fig = dt.create_figure(layout=[[1],[2] ], title="Thermostat Controlled Temperature",
                           width=1600, height=600)

    fig.subplot(1).plot("temperature")
    fig.subplot(2).plot("thermostat_on")
    fig.subplot(1).plot("measured_temp")

    # display figure
    dt.display()

def main(initial_temp=60.0, heater_capacity=90.0, outside_temp=40.0,
        thermostat_on=0.0, set_temperature=60.0, hysteresis_range=15.0,
        temp_sample_period=0.1):

    temperature_state = temperature_system.State(temperature=initial_temp)
    temperature_params = temperature_system.Params(heater_capacity=heater_capacity,
                    outside_temperature=outside_temp)
    temperature = osdt.create_system(x=temperature_state, c=temperature_system.C, f=temperature_system.F, d=temperature_system.D, g=temperature_system.G, u=temperature_system.U, y=temperature_system.Y, id="temperature",
                             vars={temperature_system.Params:temperature_params} )

    controller_state = thermostat_controller.State(thermostat_on=thermostat_on, set_temperature=set_temperature)
    controller_params = thermostat_controller.Params(hysteresis_range=hysteresis_range)

    controller = osdt.create_system(x=controller_state, d=thermostat_controller.D, g=thermostat_controller.G, u=thermostat_controller.U, y=thermostat_controller.Y, id="temperature",
                             vars={thermostat_controller.Params:controller_params} , routine=thermostat_controller.routine )

    temp_sensor_state = sensor.State(value=0.0, timer=0.0)
    temp_sensor_params = sensor.Params(sample_period=temp_sample_period,
                                      sample_field=None)
    temp_sensor = osdt.create_system(x=temp_sensor_state, c=sensor.C, f=sensor.F,
                                    d=sensor.D, g=sensor.G, u=sensor.U,y=sensor.Y,
                                    id="temp_sensor",
                                    vars={sensor.Params: temp_sensor_params})


    temperature.set(temperature_system.CONTROLLER,controller)
    temp_sensor.set(sensor.INPUT, temperature)
    controller.set(thermostat_controller.TEMPERATURE, temp_sensor)

  #  dt.set_integrator(max_step=.01)
    dt.run()

    # create a figure
    fig = dt.create_figure(layout=[[1],[2] ], title="Thermostat Controlled Temperature",
                           width=1600, height=600)

    fig.subplot(1).plot("temperature")
    fig.subplot(2).plot("thermostat_on")
    fig.subplot(1).plot("measured_temp")

    # display figure
    dt.display()
if __name__ == "__main__":
    main()




