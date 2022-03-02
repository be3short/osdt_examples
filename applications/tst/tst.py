import osdt,sys

class T:
    not_modeled = ["measured_temp"]
    def __init__(self, a=0.0):
        self.a=a

def main(obj_path = None):
    y=osdt.utils.read_yaml_file(obj_path)
    print(y)
    print(' '.join(sys.argv[1:]))
def main1(main1arg=1.0 ):

    st = T()
    stc = type(st)
    print(stc.__dict__)
