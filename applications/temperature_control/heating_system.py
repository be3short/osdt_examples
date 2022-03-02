import osdt
import osdt as dt

from osdt_examples.models import heater_system, heater_controller


def main(initial_temp=60.0, heater_capacity=90.0, outside_temp=40.0,
        thermostat_on=0.0, set_temperature=60.0, hysteresis_range=15.0):

    heater = heater_system.create(initial_temp, heater_capacity, outside_temp)
    controller = heater_controller.create(thermostat_on, set_temperature, hysteresis_range)

    heater_system.connect_controller(heater, controller)
    heater_controller.connect_heater(controller,heater)

    dt.run()

    # create a figure
    fig = dt.create_figure(layout=[[1],[2] ], title="Thermostat Controlled Temperature",
                           width=1600, height=600 )

    fig.subplot(1).plot("temperature")
    fig.subplot(2).plot("thermostat_on")

    fig.export("figure1",format="png")

    # display figure
    dt.display()


"""

def test(initial_temp=60.0 ):
    print(initial_temp)

def main_simple(initial_temp=60.0, heater_capacity=90.0, outside_temp=40.0,
        thermostat_on=0.0, set_temperature=60.0, hysteresis_range=15.0):
    temperature_state = heater_system.State(temperature=initial_temp)
    temperature_params = heater_system.Params(heater_capacity=heater_capacity,
                    outside_temperature=outside_temp)
    temperature = osdt.create_system(x=temperature_state, c=heater_system.C, f=heater_system.F, d=heater_system.D, g=heater_system.G, u=heater_system.U, y=heater_system.Y, id="temperature",
                             vars={heater_system.Params:temperature_params} )

    controller_state = heater_controller.State(thermostat_on=thermostat_on, set_temperature=set_temperature)
    controller_params = heater_controller.Params(hysteresis_range=hysteresis_range)

    controller = osdt.create_system(x=controller_state, d=heater_controller.D, g=heater_controller.G, u=heater_controller.U, y=heater_controller.Y, id="temperature",
                             vars={heater_controller.Params:controller_params} , routine=heater_controller.routine )

    temperature.set(heater_system.CONTROLLER,controller)
    controller.set(heater_controller.TEMPERATURE,temperature)

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
        thermostat_on=0.0, set_temperature=60.0, hysteresis_range=15.0):

    heater = heater_system.create(initial_temp, heater_capacity, outside_temp)
    controller = heater_controller.create(thermostat_on, set_temperature, hysteresis_range)
    heater_sensor = sensor.create(sample_field=None,sample_interval=0.2,input=heater)
    controller_sensor = sensor.create(sample_field=None,sample_interval=0.2,input=controller)

    heater_system.connect_controller(heater, controller_sensor)
    heater_controller.connect_heater(controller,heater_sensor)

    dt.run()

    # create a figure
    fig = dt.create_figure(layout=[[1],[2] ], title="Thermostat Controlled Temperature",
                           width=1600, height=600)

    fig.subplot(1).plot("temperature")
    fig.subplot(2).plot("thermostat_on")
    fig.subplot(1).plot("value",system=heater_sensor)
    fig.subplot(2).plot("value",system=controller_sensor)

    #  fig.subplot(1).plot("measured_temp")

    # display figure
    dt.display()
    
    

def main_2(initial_temp=60.0, heater_capacity=90.0, outside_temp=40.0,
        thermostat_on=0.0, set_temperature=60.0, hysteresis_range=15.0,
        temp_sample_period=0.1):

    temperature_state = heater_system.State(temperature=initial_temp)
    temperature_params = heater_system.Params(heater_capacity=heater_capacity,
                    outside_temperature=outside_temp)
    temperature = osdt.create_system(x=temperature_state, c=heater_system.C, f=heater_system.F, d=heater_system.D, g=heater_system.G, u=heater_system.U, y=heater_system.Y, id="temperature",
                             vars={heater_system.Params:temperature_params} )

    controller_state = heater_controller.State(thermostat_on=thermostat_on, set_temperature=set_temperature)
    controller_params = heater_controller.Params(hysteresis_range=hysteresis_range)

    controller = osdt.create_system(x=controller_state, d=heater_controller.D, g=heater_controller.G, u=heater_controller.U, y=heater_controller.Y, id="temperature",
                             vars={heater_controller.Params:controller_params} , routine=heater_controller.routine )

    
    temp_sensor_state = sensor.State(value=0.0, timer=0.0)
    temp_sensor_params = sensor.Params(sample_period=temp_sample_period,
                                      sample_field=None)
    temp_sensor = osdt.create_system(x=temp_sensor_state, c=sensor.C, f=sensor.F,
                                    d=sensor.D, g=sensor.G, u=sensor.U,y=sensor.Y,
                                    id="temp_sensor",
                                    vars={sensor.Params: temp_sensor_params})
    temp_sensor.set(sensor.INPUT, temperature)
    temperature.set(heater_system.CONTROLLER,controller)
    controller.set(heater_controller.TEMPERATURE, temp_sensor)

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


"""

