import sys,os

import osdt
import yaml

from osdt_example_lib.models import bouncing_ball as bb
import osdt as dt

from random import random
log=osdt.get_logger()
def main1(y_position=1.0,
        y_velocity=0.0,
        gravity=9.81,
        restitution=.95,
        t=5.0,
        j=20):

    ball = osdt.utils.perform_task("tasks/create_bouncing_ball.yaml")

    dt.run(t=t, j=j)

    # create a figure
    fig = dt.create_figure(layout=[[1,3,4,4], [2,3,4,4]],title="Bouncing Ball",
                           width=1600, height=600)

    fig.subplot(1).plot("y_position",max_points=200)
    fig.subplot(2).plot("y_velocity",max_points=200)
    fig.subplot(3).plot(["y_position", "y_velocity"],max_points=200)
    fig.subplot(4).plot(x="y_velocity", y="y_position",max_points=200)
    #fig.export("output/single_bouncing_ball/figure.pdf",format="pdf")
    print(dt.toolbox.global_operator.integrator._integrator.__dict__)
    dt.display()
def main(y_position=1.0,
        y_velocity=0.0,
        gravity=9.81,
        restitution=.95,
        t=5.0,
        j=20):
  #  ball_args=yaml.safe_load(open("tasks/createsys.yaml", 'r'))
    #for sys_id in ball_args:
   #     ball=create_sys(**ball_args[sys_id],id=sys_id)
   # ball = osdt.utils.perform_task("tasks/create_bouncing_ball.yaml")

    ball = osdt.utils.perform_task("tasks/create_bouncing_ball.yaml")

    balls=osdt.utils.perform_task("tasks/createsystems.yaml")

    dt.run(t=t, j=j)

    # create a figure
    fig = dt.create_figure(layout=[[1,3,4,4], [2,3,4,4]],title="Bouncing Ball",
                           width=1600, height=600)

    fig.subplot(1).plot("y_position",max_points=200)
    fig.subplot(2).plot("y_velocity",max_points=200)
    fig.subplot(3).plot(["y_position", "y_velocity"],max_points=200)
    fig.subplot(4).plot(x="y_velocity", y="y_position",max_points=200)
    #fig.export("output/single_bouncing_ball/figure.pdf",format="pdf")
    print(dt.toolbox.global_operator.integrator._integrator.__dict__)
    dt.display()


def get_module_obj(obj_str):
    obj=None
    try:
        parts=obj_str.split(".")
        obj_name=parts[len(parts)-1]
        module_name=obj_str[0:(len(obj_str)-len(obj_name)-1)]
        __import__(module_name)
        loaded_obj=getattr(sys.modules[module_name],obj_name)
        obj=loaded_obj
    except:
        log.debug("unable to get module object: "+str(obj_str))
    return obj

def replace_arg_values(args):
    if type(args) is list:
        new_list = []
        for arg_obj in args:
            new_arg_obj = replace_arg_values(arg_obj)
            new_list.append(new_arg_obj)
        return new_list
    elif type(args) is dict:
        new_args={}
        for arg_key in args:
            arg_obj = args[arg_key]
            new_arg_obj = replace_arg_values(arg_obj)
            new_args[arg_key]=new_arg_obj
        return new_args
    elif type(args) is str:
        new_obj = args

        if args.startswith("#") and args.endswith("#"):
            module_obj=get_module_obj(args[1:len(args)-1])
            if module_obj is not None:
                new_obj=module_obj
        elif args.startswith("$") and args.endswith("$"):
            try:
                true_val = args[1:len(args)-1]
                module_func = true_val.split("$")[0]
                args = true_val.split("$")[1]
                func=get_module_obj(module_func)
                potential_obj=func(args)
                new_obj=potential_obj
            except:
                pass
        return new_obj

    else:
        return args

def create_systems(**system_args):
    conns=system_args["connections"]
    print(conns)
    sysargs={}
    for arg_key in system_args:
        print(arg_key)
        if arg_key != 'connections':
            sysargs[arg_key]=system_args[arg_key]
    print("sys_args\n"+str(sysargs))
    systems = replace_arg_values(sysargs)
    print("systems\n"+str(systems))
    new_systems={}
    for sys_id in systems.keys():
        kwargs=systems[sys_id]
        kwargs["id"]=sys_id
        new_sys=create_sys(**kwargs)
        new_systems[sys_id]=new_sys
    print(new_systems)
    conndata=replace_arg_values(conns)
    print(conndata)
    return new_systems

def create_systems_working(**system_args):
    print(system_args)
    systems = replace_arg_values(system_args)
    print(systems)
    new_systems={}
    for sys_id in systems.keys():
        kwargs=systems[sys_id]
      #  kwargs["id"]=sys_id
        new_sys=create_sys(**kwargs)
        new_systems[sys_id]=new_sys
    return new_systems
def create_sys(x=None, c=None, f=None, d=None, g=None, u=None, y=None,
        vars={},x_vals={},var_vals={},id=None):
        state = get_module_obj(x)(**x_vals)
        var_objs = {}
        for var_key in vars:
            vals = {}
            if var_key in var_vals:
                vals = var_vals[var_key]
            var_obj = get_module_obj(vars[var_key])(**vals)
            var_objs[var_key]=var_obj
        return osdt.create_system(x=state,c=c,f=f,d=d,g=g,u=u,y=y,vars=var_objs,id=id)

if __name__ == "__main__":
    main()



