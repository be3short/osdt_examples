import sys

import osdt
import osdt as dt

from osdt_examples.models import heater_system, heater_controller,sensor
def ddd(qq1,avc=4):
    return qq1

def figure():
    fig = dt.create_fig(layout=[[1], [2]], title="Thermostat Controlled Temperature")
    fig.plot(1,"temperature")
    fig.plot(1,"measured_temp")
    fig.plot(1,"value", system="heater_sensor")
    fig.plot(2,"thermostat_on")
    fig.plot(2,"value", system="controller_sensor")
  #  fig.export("figure1", format="png")
    return fig

def connect(app ):
    app.heater.controller = app.controller_sensor
    app.controller_sensor.input_sys=app.controller
    app.controller.heater = app.heater_sensor
    app.heater_sensor.input_sys=app.heater

def heater_app():
    app = dt.app(
        heater=dt.create_sys(heater_system),
        controller=dt.create_sys(heater_controller),
        heater_sensor=sensor.new(id="heater_sensor"),
        controller_sensor = sensor.new(id="controller_sensor"),
        figure=figure()
    )
    app.add_setup(connect)
    return app

import yaml

if __name__ == "__main__":
    app = heater_app()
    dt.get_config().run.time=20.0
    app.run(True)

    #osdt.dataset.clear_data()
#    dt.get_env().prepare_environment()
 #   print(dt.objects.get_child_map(app))
 #   yaml.dump(app,open("../appfiles/qa.yaml","w"))#, default_style="ruamel.yaml")

 #   app.save("../appfiles/qr.json")

    #q=e=osdt.load("../appfiles/hsr.json")
    #p=yaml.unsafe_load((open("../appfiles/q.yaml","r")))
    #print(p.__dict__)
    #p.display()
   # figure()
   # osdt.display()









