import osdt as dt
from osdt_examples.models import ball

if __name__ == "__main__":
    ball1= ball.create()
    dt.add_systems(ball1)
    dt.run()
    ball.plot()
    dt.display()


