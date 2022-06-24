import osdt #as dt

from osdt_examples.models import point_mass as pm

def figure():
    xyfig = osdt.create_fig(layout=[[1]], title="Point Mass Interaction", dpi=130)
    xyfig.plot(1, x="x_position", y="y_position")
def setup(app):
    pm.connect_all_masses()
    osdt.get_config().integrator.max_step=100.0
    osdt.get_config().run.time=10000.0

def pointmass_app():
    app=osdt.app()
    V_0 = .1
    state1 = pm.State(x_position=1000.0, y_position=1000.0, x_velocity=-V_0, y_velocity=V_0)
    params1 = pm.Params(mass=1100020100.0)
    app.system1 = osdt.create_sys(x=state1, c=pm.C, f=pm.F, u=pm.U, params=params1, id="small mass 1")

    state2 = pm.State(x_position=-1000.0, y_position=-1000.0, x_velocity=V_0, y_velocity=-V_0)
    params2 = pm.Params(mass=1100020110.0)
    app.system2 = osdt.create_sys(x=state2, c=pm.C, f=pm.F, u=pm.U, params=params2, id="small mass 2")

    state3 = pm.State(x_position=1000.0, y_position=-1000.0, x_velocity=V_0, y_velocity=V_0)
    params3 = pm.Params(mass=1100020100.0)
    app.system3 = osdt.create_sys(x=state3, c=pm.C, f=pm.F, u=pm.U, params=params3, id="small mass 3")

    state4 = pm.State(x_position=-1000.0, y_position=1000.0, x_velocity=-V_0, y_velocity=-V_0)
    params4 = pm.Params(mass=1100020100.0)
    app.system4 = osdt.create_sys(x=state4, c=pm.C, f=pm.F, u=pm.U, params= params4, id="small mass 4")

    state0 = pm.State(x_position=0.1, y_position=0.1, x_velocity=0.0, y_velocity=0.0)
    params0 = pm.Params(mass=911000220100.0)
    app.system0 = osdt.create_sys(x=state0, c=pm.C, f=pm.F, u=pm.U, params=params0, id="large mass")
    app.fig=figure()
    app.add_setup(setup)
    return app

if __name__ == "__main__":
    app = pointmass_app()
    app.run(True)
