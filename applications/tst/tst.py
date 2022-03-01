import osdt
from osdt_examples.models import thermostat_controller
class T:
    not_modeled = ["measured_temp"]
    def __init__(self, a=0.0):
        self.a=a


def main( ):

    st = T()
    stc = type(st)
    print(stc.__dict__)
