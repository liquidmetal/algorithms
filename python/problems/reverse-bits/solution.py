#!/usr/bin/python

# https://leetcode.com/problems/reverse-bits/

def reverse_uint(num):
    """ Given the num is 32 bits in size """
    ret = 0

    num_bits = 4
    for i in xrange(num_bits):
        ret = ret << 1
        binary = num & 1
        num = num >> 1

        ret = ret | binary
    return ret

print(reverse_uint(3))
