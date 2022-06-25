import jsonpickle
import osdt as dt
from osdt_examples.apps import dubins, heating_system_sensor, heating_system


# from osdt_examples.models import dubins_vehicle, dubins_controller, heating


def setup(appz):
    appz.dubins2.run_setup()
    appz.heater3.run_setup()
    appz.dubins3.run_setup()
    appz.heater.run_setup()
  #  for a in appz.__dict__.values():
   #     try:
    #        a.run_setup()
     #   except:
      #      print('oops')

#    appz.heater.run_setup()
#    appz.dubins2.run_setup()


def multi():
    app = dt.app(
      #  heater=heating_system_sensor.heater_app(),
        dubins2=dubins.dubins(),
        heater3=heating_system_sensor.heater_app(),
        dubins3=dubins.dubins(),
        heater=heating_system.heater_app()
    )

    '''
  #  app.subsys = dt.var()
 #   app.subsys.set(
#        heater=heating_system_sensor.heater_app(),
 #       dubins=dubins.dubins()
  #  )
`   '''
    app.add_setup(setup)
    return app

if __name__ == "__main__":
    app = multi()#
   # app = dt.load("multi.json")
    #app.heater.add_setup(heating_system_sensor.connect)


   # app=dt.load("multi.json")#multi()
    app.run_setup()
#    app.save("multi")
    #app.run(True)
    jsonpickle.dumps(app,indent=4)
    #jsonpickle.encode(app,"jsonp.json")
