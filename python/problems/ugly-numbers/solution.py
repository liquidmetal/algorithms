#!/usr/bin/python

# Problem: https://leetcode.com/problems/ugly-number/
import math

def is_ugly(num):
    """2, 3, 5 are the only prime factors"""

    if num == 0:
        return False

    if num == 1:
        return True


    for i in [2, 3, 5]:
        import pdb; pdb.set_trace()
        while num % i == 0:
            num = num / i

    if num != 1:
        return False

    return True

print is_ugly(-2147483648)
