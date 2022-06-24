import osdt as dt
from osdt_examples.apps import dubins, heating_system_sensor


# from osdt_examples.models import dubins_vehicle, dubins_controller, heating


def setup(appz):
    for a in appz.__dict__.values():
        try:
            a.run_setup()
        except:
            print('oops')
  #  appz.heater.run_setup()
  #  appz.dubins2.run_setup()


@dt.root
def multi():
    app = dt.app(
        heater=heating_system_sensor.heater_app(),
        dubins2=dubins.dubins()
    )
    '''
    app.set(
        heater2=heating_system_sensor.heater_app(),
        dubins2=dubins.dubins()
    )
    '''
  #  app.subsys = dt.var()
 #   app.subsys.set(
#        heater=heating_system_sensor.heater_app(),
 #       dubins=dubins.dubins()
  #  )

    app.add_setup(setup)
    return app


if __name__ == "__main__":
    app = multi()
    app.save("multi")
   # app.run(True)
