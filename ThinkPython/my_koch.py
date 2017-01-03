from swampy.TurtleWorld import *

def koch(t, length):
    if length < 3 :
        fd(t, length)
        return
    koch(t, length / 3)
    lt(t, 60)
    koch(t, length / 3 )
    rt(t, 120)
    koch(t, length / 3)
    lt(t, 60)
    koch(t, length / 3 )


world = TurtleWorld()    
bob = Turtle()
bob.delay = 0.0001
koch(bob, 1000)
wait_for_user()
