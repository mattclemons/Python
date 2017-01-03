import math
# As an example, suppose you want to find the distance
# between two points, given by the coordinates (x1, y1) and (x2, y2).
# By the Pythagorean theorem, the formula for distance is:
# distance = square root of(x sub2 - x sub1)squared + (y sub2 - y sub1)squared


def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result
