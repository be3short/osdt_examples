import osdt,sys
from osdt_examples.models import sensor
class T:
    not_modeled = ["measured_temp"]
    def __init__(self, a=0.0):
        self.a=a


def main():
    #osdt.figure.set_style("sysfiles/increase_font_size.style")#osdt.get_path("sysfiles/increase_font_size.style"))

    #osdt.constructor.construct_systems("sysfiles/ball_w_sensors.yaml",ball1="ball1",ball2="ball1",pos_sensor="pos_sensor",vel_sensor="vel_sensor",pos_sensor2="pos_sensor",vel_sensor2="vel_sensor",system_args={"ball2":{"key":"ball1","label":"Ball 2"}})
    osdt.constructor.construct_systems("sysfiles/ball_w_sensors.yaml")#,ball1="ball1",ball2="ball1",pos_sensor="pos_sensor",vel_sensor="vel_sensor",pos_sensor2="pos_sensor",vel_sensor2="vel_sensor",system_args={"ball2":{"key":"ball1","label":"Ball 2"}})
    #osdt.constructor.construct_systems("sysfiles/ball_w_sensors.yaml",ball2="ball1",pos_sensor2="pos_sensor",vel_sensor2="vel_sensor",system_args={"ball2":{"key":"ball1","label":"Ball 2"}})
    osdt.constructor.construct_connections({"sysfiles/ball_w_sensors.yaml":["connections"]})
    #osdt.create_connections(["pos_sensor2","ball2",sensor.INPUT],["vel_sensor2","ball2",sensor.INPUT])
    osdt.run()
    figg=osdt.construct_figures("sysfiles/figure.yaml","figure2")



 #   fig.set_style( osdt.get_path("sysfiles/increase_font_size.style"))
    #osdt.display()

alias={"subplots": "configure_subplot"}
def main3(obj_path = None,figures=[]):
    y = osdt.utils.read_yaml_file(obj_path)
    for figure_key in figures:
        fig_data = y[figure_key]
        fig = osdt.create_figure(**fig_data["figure"])
        for call in fig_data:
            if call != "figure":
                argset = fig_data[call]
                if call in alias:
                    func=getattr(fig,alias[call])
                else:
                    func=getattr(fig,call)
                if type(argset) is dict:
                    argset=[argset]
                for args in argset:
                    func(**args)

def main2(obj_path = None):

    y=osdt.utils.read_yaml_file(obj_path)
    fig_data=y["figure"]
    fig=osdt.create_figure(**fig_data["figure"])
    config = fig_data["subplots"]
    for config_vals in config:
        subplot = config_vals["i"]
        del config_vals["i"]
        fig.configure_subplot(subplot,**config_vals)
    plot=fig_data["plot"]
 #   for subplot in plot:
    items = plot#[subplot]
    for item in items:
        subplot=item["i"]
        del item["i"]
        fig.plot(subplot,**item)
    if "export" in fig_data:
        fig.export(**fig_data["export"])
  #  f=osdt.create_figure()
  #  f.plot(1,y="value1")
  #  f.plot(1,y="value2")
  #  print(osdt.figure.figure_commands)
def main2(obj_path = None):
    y=osdt.utils.read_yaml_file(obj_path)
    print(y)
def main1(main1arg=1.0 ):

    st = T()
    stc = type(st)
    print(stc.__dict__)
