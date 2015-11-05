#!/usr/bin/python

cached = {}

def rob(nums):
    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return nums[0]

    p1 = rob(nums[:-2]) + nums[-1]
    p2 = rob(nums[:-1])
    return max(p1, p2)

print rob([2,4,8,9,9,3])
