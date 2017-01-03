from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print(bob)
def square(t, length, degrees):
    t = Turtle()
    for i in range(4):
        fd(t, length)
	lt(t, degrees)

square(bob, 100, 90)
wait_for_user()