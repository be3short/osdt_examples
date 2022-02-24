import copy

import osdt
import yaml


from osdt_examples.models import ball,sensor



if __name__ == "__main__":
    #
    if True:
        osdt.constructor.build_figure_file(layout=[[1],[2]],args={"pos_system":[],"vel_system":[]},path="fig12")
        osdt.constructor.create_environment_opfile(
            systems={"ball": ball.opfile, "pos_sensor": sensor.opfile,
                     "vel_sensor": sensor.opfile}, connections=2, integrator=True,
            run=True,opfile_calls={"fig":"osdt_examples/fig10.yaml"}, path="test13")

    b=osdt.constructor.OpfileBuilder()
    b.add_sys("ball",ball,ball.State,variables={ball.Params:ball.Params()})
    b.add_sys("ball2", ball, ball.State(), ball.Params,params2=ball.Params)
    b.add_sys("pos_sensor",sensor,sensor.State,sensor.Params(sample_field="y_position"))
    b.add_sys("vel_sensor",sensor,sensor.State,sensor.Params(sample_field="y_velocity"))
    b.add_func(None,osdt.create_connections,connection_matrix=[["v:pos_sensor","p:osdt_examples.models.sensor.INPUT","v:ball"],["v:vel_sensor","p:osdt_examples.models.sensor.INPUT","v:ball"]],yaml_args=osdt.constructor.SAFE_ARGS)
    #b.add_connections(2)
    b.add_func(None,"osdt.run")
    b.add_file("fig","osdt_examples/fig10.yaml")
    b.create_opfile("opfile_test1")
    #print(yaml.safe_dump(osdt.constructor.create_opfile(["ball","osdt_examples.models.ball","osdt_examples.models.ball.State","osdt_examples.models.ball.Params"],["something","osdt.run"],[]), sort_keys=False))