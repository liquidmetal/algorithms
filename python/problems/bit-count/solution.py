#!/usr/bin/python

# https://leetcode.com/problems/number-of-1-bits/

def num_bits(n):
    # Assuming 32bit unsigned integers
    ret = 0

    m0 = 0x55555555
    m1 = 0x33333333
    m2 = 0x0f0f0f0f
    m3 = 0x00ff00ff
    m4 = 0x0000ffff

    a0 = (n >> 0) & m0
    a1 = (n >> 1) & m0
    a = a0 + a1

    b0 = (a >> 0) & m1
    b1 = (a >> 2) & m1
    b = b0 + b1

    c0 = (b >> 0) & m2
    c1 = (b >> 4) & m2
    c = c0 + c1

    d0 = (c >> 0) & m3
    d1 = (c >> 8) & m3
    d = d0 + d1

    e0 = (d >> 0) & m4
    e1 = (d >> 16) & m4
    e = e0 + e1

    return e

assert(num_bits(3) == 2)
assert(num_bits(15) == 4)
