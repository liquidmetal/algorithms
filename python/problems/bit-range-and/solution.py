#!/usr/bin/python

# https://leetcode.com/problems/bitwise-and-of-numbers-range/

def total_and_naive(m, n):
    ret = 0xffffffff
    for i in xrange(m, n+1):
        ret &= i

    return ret

def total_and(m, n):
    num_bits = 32
    ret = 0
    for i in xrange(num_bits):
        if m-n > 1:
            # We have a zero
            ret >>= 1
        else:
            # We might have a one
            ret >>= 1
            ret |= ((m&1) & (n&1) << (num_bits-i))

        m >>= 1
        n >>= 1

    return ret

print total_and(5, 7)
