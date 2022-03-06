import osdt

def main():
    for syst in osdt.get_systems().values():
        print(syst.get(None))
    osdt.run()
    xyfig = osdt.create_figure(width=1200, height=800,
                               layout=[[1, 1, 3, 3], [2, 2, 3, 3]],
                               title="Point Mass Interaction", dpi=100)
    xyfig.plot(1, y="x_position", max_points=2000)
    xyfig.plot(2, y="y_position", max_points=2000)
    xyfig.plot(3, x="x_position", y="y_position", max_points=2000)
  #  xyfig.export("xy_figure", format="png")
    # xyfig.plot(1,"y_position")

  #  osdt.display()
