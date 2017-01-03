# Exercise 6.2. Use incremental development to write a function called hypotenuse
# that returns the length of the hypotenuse of a right triangle given the
# lengths of the two legs as arguments. Record each stage of the development
# process as you go.

import math

def hypotenuse(x,y):
    return math.sqrt(x**2 + y**2)

print hypotenuse(7, 10)
