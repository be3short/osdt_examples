import osdt




def main(path = None):


   # descriptor.create_constructor_file(path, ball=ball,
   #     pos_sensor=sensor.create(None,sensor.Params(sample_field="y_position"),id="pos_sensor"),
   #     vel_sensor=sensor.create(None,sensor.Params(sample_field="y_velocity"),id="vel_sensor"))
    ballsys = osdt.construct_systems(path,ball="ball",pos_sensor="pos_sensor",vel_sensor="vel_sensor")

    print(ballsys.get(None))


