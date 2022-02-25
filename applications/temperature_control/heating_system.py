import osdt as dt

from osdt_examples.models import temperature_system,thermostat_controller
from random import random

import osdt.constructor


def run(initial_temp=60.0, heater_capacity=90.0, outside_temp=40.0,
        thermostat_on=0.0, set_temperature=60.0, hysteresis_range=15.0,
        t=10.0, j=60,q=[1,2,3]):

    temperature = temperature_system.create(initial_temp=initial_temp,
                                            heater_capacity=heater_capacity,
                                            outside_temp=outside_temp)
    controller = thermostat_controller.create(thermostat_on=thermostat_on,
                                              set_temperature=set_temperature,
                                              hysteresis_range=hysteresis_range)

    temperature.set(temperature_system.CONTROLLER,controller)
    controller.set(thermostat_controller.TEMPERATURE,temperature)

    dt.run(time=t, jumps=j)

    # create a figure
    fig = dt.create_figure(layout=[[1],[2] ], title="Thermostat Controlled Temperature",
                           width=1600, height=600)

    fig.subplot(1).plot("temperature")
    fig.subplot(2).plot("thermostat_on")

    # display figure
    dt.display()
    print(q)


def create_opfile():
    op = osdt.constructor.OpfileBuilder()
    op.add_sys("temperature",temperature_system,temperature_system.State(),temperature_system.Params)
    op.add_sys("controller",thermostat_controller,thermostat_controller.State(),thermostat_controller.Params)
    op.add_func(None,osdt.create_connections,connection_matrix=[["v:temperature","p:osdt_examples.models.temperature_system.CONTROLLER","v:controller"],["v:controller","p:osdt_examples.models.thermostat_controller.TEMPERATURE","v:temperature"]],yaml_args=osdt.constructor.SAFE_ARGS)
    op.add_func(None, osdt.run)
    #osdt.constructor.build_figure_file(layout=[[1],[2]],path="applications/temperature_control/figure1.yaml")
    op.add_file("figure","osdt_examples/applications/temperature_control/figure1.yaml")
    op.create_opfile("applications/temperature_control/heater.yaml")

if __name__ == "__main__":

#    osdt.constructor.build_figure_file(layout=[[1],[2]],path="osdt_examples/applications/temperature_control/figure1.yaml")

    create_opfile()
    #run()




