import osdt
from osdt_examples.models import temperature_system,thermostat_controller,sensor

def create_sensor(sample_field=None, sample_interval=.25, input=None, id="sensor"):
    sensor_state = sensor.State(value=0.0, timer=0.0)
    sensor_params = sensor.Params(sample_period=sample_interval,
                                       sample_field=sample_field)
    sensor_system = osdt.create_system(x=sensor_state, c=sensor.C, f=sensor.F, d=sensor.D, g=sensor.G, u=sensor.U, y=sensor.Y, id=id, vars={sensor.Params: sensor_params})
    if input is not None:
        sensor_system.set(sensor.INPUT,input)
    return sensor_system