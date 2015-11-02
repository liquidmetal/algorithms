#!/usr/bin/python

import math

def power(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    elif y == -1:
        return 1.0/x

    if y > 0:
        temp = power(x, math.floor(y/2))
        ret = temp*temp
    else:
        temp = power(x, -math.floor(y/2))
        ret = 1.0/(temp*temp)

    if y % 2 == 0:
        return ret
    else:
        if y > 0:
            return ret*x
        else:
            return ret/x


assert(power(2, 4) == 16)
assert(power(3, 3) == 27)
assert(power(100, 0) == 1)
assert(power(1, -1) == 1)
assert(power(2, -4) == 1.0/(2*2*2*2))
