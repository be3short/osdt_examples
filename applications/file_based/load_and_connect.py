import osdt
from osdt_examples.models import ball
def main(def_file = "",
         systems_key="systems",
         system_args_key="system_args",
         connections_key="connections",
         figures_key="figures",
         system_def_file = "sysfiles/ball_w_sensors.yaml",
         system_args_file="sysfiles/ball_w_sensors.yaml",
         connections_file="sysfiles/ball_w_sensors.yaml",
         figure_file="sysfiles/figure.yaml"):
    conns = []
class Test2:
    def __init__(self,val3=3):
        self.val3=3

class Tester:
    def __init__(self,val1=1,val2 = "2",val3=Test2()):
        print(val3)

def create(val1=1,val2 = "2",val3=Test2(),test4=Tester()):
    print(val3.__dict__)
    print(test4.__dict__)

def main(create_file="", module_name="osdt_examples.applications.file_based.load_and_connect",read_file=""):  ##.ball.__name__, read_file=""


    #arg_dat=osdt.arguments.FunctionArgData(ball.create)
    #print(arg_dat.non_positional_args)

    #ball1=ball.create()
    #ball2=ball.create()
    #ball2.x().y_position=10.0
    #ball1.x().y_position=1.0
    function_arg_data=osdt.arguments.FunctionArgData(ball.create)
  #  print(function_arg_data.get_all_args())
    func=osdt.utils.get_module_component(module_name,"create")#getattr(osdt.utils.get_module_obj(module_name + ".create"))
    if len(create_file)>0 and module_name is not None:
        primargs=osdt.arguments.get_primitive_system_create_args(func)
        osdt.utils.write_yaml_file(primargs,create_file)
    if len(read_file)>0:
        primargs2 = osdt.utils.read_yaml_file(read_file)
        print(primargs2)
        finalargs=osdt.arguments.get_create_args_from_primitive(create,primargs2)
        print(finalargs)
        sys=func(**finalargs)
    #    print(sys.x().__dict__)

    point_mass.connect_all_masses()

    # print(osdt.system.get_model(sys).initialize_function)
    osdt.run()
    #print(ball1.x().y_position)
    #osdt.run()

    osdt.construct_figures("osdt_examples/sysfiles/figure.yaml","figure1")
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