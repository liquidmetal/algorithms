#!/usr/bin/python

import math

def memoize(func):
    table = {}
    def wrapper(height, width):
        if width not in table:
            table[width] = {}

        if height not in table[width]:
            table[width][height] = func(height, width)

        return table[width][height]

    return wrapper

def width_perm(width):
    if width < 0:
        return 0

    if width == 0 or width == 1:
        return 1

    return width_perm(width-1) + width_perm(width-2) + width_perm(width-3) + width_perm(width-4)

def height_perm(height, width):
    out = math.pow(width_perm(width), height)
    return out

@memoize
def solid_width(height, width):
    first = height_perm(height, width)

    summation = 0
    for i in xrange(1, width):
        summation += solid_width(height, i) * height_perm(height, width-i)

    return first - summation

if __name__ == '__main__':
    assert(width_perm(1) == 1)
    assert(width_perm(2) == 2)
    assert(width_perm(3) == 4)
    assert(width_perm(4) == 8)
    assert(width_perm(5) == 15)
    assert(width_perm(6) == 29)

    assert(solid_width(1, 2) == 1)
    assert(solid_width(1, 3) == 1)
    assert(solid_width(1, 4) == 1)
    assert(solid_width(1, 5) == 0)

    assert(solid_width(2, 2) == 3)
    assert(solid_width(2, 3) == 9)
