#!/usr/bin/python

# Original problem
# https://www.hackerrank.com/challenges/flipping-bits

import math

num_bits = 32
T = input()
upper = math.pow(2, num_bits)
for i in xrange(T):
    num = input()

    print(int(upper - num - 1))
