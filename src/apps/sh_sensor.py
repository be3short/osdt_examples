import osdt as dt
from osdt_examples.models import sensor



@dt.task
def attach_sensors(
        measured_sys = None,
        measured_values = [],
        sensor_params = sensor.Params()):

    sensors = dt.var()
    for value in measured_values:

        sensor_sys = sensor.create(params=sensor_params.copy(),id="sensor_{}".format(value))
        sensor_sys.params.set(sample_field=value)
        sensor_sys.connector.connect(measured_sys)
        sensors.set(sensor_sys.get_id(),sensor_sys)

    return sensors





    '''
    if app is None: app = dt.app(
        func=attach_sensors
        measured_sys = None,
        measured_values = [],
        sensor_params = sensor.Params()
    )
    else:
    '''



