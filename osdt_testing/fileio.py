import logging as log
import osdt
from osdt_examples.models import ball

SAVED_OBJ="saved_obj"
LOAD_OBJ = "osdt_examples/osdt_testing/files/"+SAVED_OBJ
SAVED_ENV="saved_env"
LOAD_ENV = "osdt_examples/osdt_testing/files/"+SAVED_ENV



def get_object():
    ball_sys=ball.State()
    return ball_sys
def get_system():
    ball_sys=ball.create()
    ball_sys.x().y_position=11.1
    ball_sys.x().y_velocity=22.2
    return ball_sys
def check_save_load_obj():
    orig=save_obj()
    loaded=load_obj()
    passed=True
    for key in orig.__dict__:
        passed=passed and (orig.__dict__[key]==loaded.__dict__[key])
    return passed

def check_save_load_env():
    orig=save_env()
    orig_env = osdt.get_environment()
    orig_state=orig_env.get_system(orig.get_id()).x()
    osdt.clear()
    loaded=load_env()
    passed=True
    sys1=loaded.get_system(orig.get_id())
    print(sys1)
    for key in orig.x().__dict__:
        passed=passed and (orig.x().__dict__[key]==sys1.x().__dict__[key])
    return passed

def save_obj():
    original_ball_sys = get_object()
    osdt.save_obj(original_ball_sys,SAVED_OBJ)
    return original_ball_sys

def load_obj():
    loaded=osdt.load_obj(LOAD_OBJ)
    return loaded

def save_env():
    original_ball_sys = get_system()
    osdt.save_env(SAVED_ENV,overwrite=True)
    return original_ball_sys

def load_env():
    loaded=osdt.load_env(LOAD_ENV)
    return loaded

def run_tests():
    tests = [check_save_load_obj,check_save_load_env]
    report = "running tests:\n"+osdt.logger.create_header(str(__name__))
    passed = 0
    all_results = {}
    for t in tests:
        result=t()
        report=report+"\n"+str(t.__name__)+": "+ osdt.logger.get_pass_fail_str(result)
        all_results[t.__name__]= result
        passed = passed +  1 if result else 0
    percentage = 0 if passed == 0 else 100.0*(passed / len(tests))
    report=report+"\npassed: "+str(percentage)+"%"
    log.info(report)