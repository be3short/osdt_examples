"""Input only model."""
import osdt
import copy

INPUT = "INPUT"
PARAMS="PARAMS"
class State(): # state class
    def __init__(self):
        self.value = 1.0
        self._non_dynamic=[ "value"]

def Y(x, hs, *args, **argmap): # output map (determine output value)
    return x.value

