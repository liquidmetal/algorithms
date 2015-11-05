#!/usr/bin/python

import random

def two_largest(nums):
    m1 = nums[0]
    m2 = None

    for n in nums:
        if n > m1:
            m2 = m1
            m1 = n
        elif n > m2 and n < m1:
            m2 = n


    return (m1, m2)

l = random.sample(range(10), 5)
print l
print two_largest(l)
