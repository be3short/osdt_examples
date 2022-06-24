



import osdt
import osdt as dt

from osdt_examples.models import heater_system, heater_controller,sensor

def figure():
    fig = dt.create_fig(layout=[[1], [2]], title="Thermostat Controlled Temperature")
    fig.plot(1,"temperature")
    fig.plot(1,"measured_temp")
    fig.plot(1,"value", system="temp_sensor")
    fig.plot(2,"thermostat_on")
    fig.plot(2,"value", system="controller_sensor")
  #  fig.export("figure1", format="png")
    return fig

def connect(app):
    app.heater.controller = app.controller_sensor
    app.controller.heater = app.heater


def heater_app():
    app = dt.app(
        heater=dt.build_sys(heater_system),
        controller=dt.build_sys(heater_controller),
        heater_sensor=sensor.new(),
        controller_sensor = sensor.new(),
    figure=figure()
    )
    app.add_setup(connect)

    return app

if __name__ == "__main__":
    app = heater_app()
    app.run(True)








