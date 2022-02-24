import osdt,sys

#if len(sys.argv)>2:

 #   osdt.utils.create_script_argfile(sys.argv[1],sys.argv[2])
#else:
#if sys.argv[1] == "make":
#    osdt.utils.create_script_argfile(sys.argv[2], sys.argv[3])
#else:
#    dat=osdt.utils.run_script(*sys.argv[1:])
#print(dat)
import yaml

FUNCTION_PREFIX= "f"
VARIABLE_PREFIX= "v:"
OBJECT_PREFIX= "o:"
SEPARATION_SPLITTER = ":"
PREFIXES=[FUNCTION_PREFIX,VARIABLE_PREFIX,OBJECT_PREFIX]

def run_if_func(object_val,objectfile):
    fcomp=fill_object(object_val,objectfile)
    func = fcomp[0][FUNCTION_PREFIX]
    args = []
    kwargs={}
    for ind in range(1,len(fcomp)):
        if type(fcomp[ind]) is dict:
            for key in fcomp[ind]:
                kwargs[key]=fcomp[ind][key]
        else:
            args.append(fcomp[ind])
    func(*args,**kwargs)
def fill_object(object_val,objectfile):
    object_val_filled =object_val
    if type(object_val) is str:
        if object_val.startswith(VARIABLE_PREFIX):
            object_val_filled=get_variable_value(object_val,objectfile)
        elif object_val.startswith(OBJECT_PREFIX):
            object_val_filled=get_python_object(object_val,objectfile)
    elif osdt.utils.is_primitive(object_val):
        object_val_filled = object_val
    elif type(object_val) is dict:
        if len(object_val)==1 and FUNCTION_PREFIX in object_val:
            object_val_filled = object_val[FUNCTION_PREFIX]
            object_val_filled=fill_object(object_val_filled,objectfile)
            object_val_filled=osdt.utils.get_function(object_val_filled)
          #  object_val[FUNCTION_PREFIX]=object_val_filled
            object_val_filled = {FUNCTION_PREFIX: object_val_filled}
        else:
            final_dict = {}
            for key in object_val:
                val =object_val[key]
                final_val = fill_object(val,objectfile)
                final_dict[key]=final_val
            object_val_filled= final_dict
    elif type(object_val) is list:
        object_val_filled= handle_list(object_val,objectfile)
    print(object_val_filled)
    return object_val_filled

def handle_list(object_val,objectfile):
    final_list=[]
    if type(object_val) is list:
        for list_val in object_val:
            final_val = fill_object(list_val,objectfile)
            final_list.append(final_val)
    return final_list

def get_python_object(object_val, objectfile):
    print(object_val[len(OBJECT_PREFIX):])
    return osdt.utils.get_function(object_val[len(OBJECT_PREFIX):])
def get_variable_value(object_val, objectfile):
    components = object_val.split(SEPARATION_SPLITTER)
    parent_key = components[1]
    parent = objectfile[parent_key]
    for ind in range(2,len(components)):
        next_key = components[ind]
        if next_key in parent:
            parent=parent[next_key]
    print(parent)
    final_val=fill_object(parent,objectfile)
    return final_val


setup = {"ball":"osdt_example.models.bouncing_ball","pos_sensor":"osdt_example.models.sample_hold_sensor","vel_sensor":"osdt_example.models.sample_hold_sensor"}
constructor={}
for s in setup:
    constructor[s]=osdt.utils.generate_sys_args(setup[s],"State","Params")
osdt.utils.write_yaml_file(constructor,"systems")
#print(a)


def call_script(path,args):#"osdt_example/testargs.yaml"):
    #argzs=osdt.load_objfile(arg_path)["fig_args"]
    ob=osdt.load_objfile(path,args=args)
    ret_val=ob["return"]
    osdt.display()
    return ret_val



def readfile(path=None):
    if path is None:
        path = sys.argv[1]

    final_contents=osdt.opfile.load_opfile(path)

    print(final_contents)


#readfile()
#call_script("osdt_example/test.yaml")