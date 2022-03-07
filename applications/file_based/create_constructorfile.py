import osdt
from osdt_examples.models import ball,timer,point_mass

def main(path="argtest3.yaml", read=0, module="osdt_examples.models.ball",key="system",run=0):  ##.ball.__name__, read_file=""

    osdt.set("g",ball.Params(restitution=1.1))
    if True:
        func=osdt.utils.get_module_component(module,"create")#getattr(osdt.utils.get_module_obj(module_name + ".create"))
        if read==0 and len(path)>0:
            primargs=osdt.arguments.get_primitive_system_create_args(func)
            primargs[osdt.defs.OSDT_CALL]=module+".create"
            #prim_dict = {key:primargs}
            fileargs={}
            try:
                az = osdt.utils.read_yaml_file(path)
                if az is not None:
                    fileargs=az
            except:
                pass
            print(fileargs)
            fileargs=primargs
            print(fileargs)
            osdt.constructor.write_system_file(path,fileargs,key)#,append=True)
        if read>0:#False:#len(read_file)>0:

            primargs2 = osdt.utils.read_yaml_file(path)
            for idkey in primargs2:
                primargz=primargs2[ idkey]
                fun = osdt.utils.get_function(primargz[osdt.defs.OSDT_CALL])
                print(primargs2)
                finalargs=osdt.arguments.get_create_args_from_primitive(fun,primargz)
                print(finalargs)
                sys=fun(**finalargs)

    #    print(sys.x().__dict__)
   # print(osdt.system.get_model(sys).initialize_function)
    if run > 0:
        point_mass.connect_all_masses()

       # sys1=ball.create()
       # sys2=ball.create()
        #sys1.x().y_position=11.0
        osdt.run()
        #print(ball1.x().y_position)
        #osdt.run()
        xyfig = osdt.create_figure(width=1200, height=800, layout=[[1]],
                                   title="Point Mass Interaction", dpi=100)
        xyfig.plot(1, x="x_position", y="y_position", max_points=1000)
        xyfig.export("xy_figure", format="png")
        xyfig.plot(1,"y_position")

      #  osdt.display()

        osdt.construct_figures("osdt_examples/sysfiles/figure.yaml","figure1","figure2","figure3")
    """
  #  systems=osdt.construct_systems("osdt_examples/sysfiles/sensor_ball.yaml",
                           ball_1="ball",
                           pos_sensor_1="pos_sensor",
                           vel_sensor_1="vel_sensor",
                           connect=True)
    
    
     = osdt.construct_systems()

    osdt.run()

    osdt.construct_figures("osdt_examples/sysfiles/figure.yaml","figure1")
    print(conns)

    """