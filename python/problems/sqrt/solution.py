#!/usr/bin/python


def sqrt(num):
    if num == 0:
        return 0

    if num == 1:
        return 1

    if num < 0:
        raise Exception("Negative numbers? I'm too naive for that")

    # Begin iterating
    x_current = (num / 2) - 20
    x_next = num / 2
    epsilon = 0.00000001

    while abs(x_current-x_next) > epsilon:
        x_current = x_next
        x_next = 0.5 * (x_current + num/x_current)

    return x_next

assert(abs(sqrt(10) - 3.16227766017) < 0.000001)
assert(abs(sqrt(9) - 3.0) < 0.000001)
