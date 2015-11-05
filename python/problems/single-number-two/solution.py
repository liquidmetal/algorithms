#!/usr/bin/python

# https://leetcode.com/problems/single-number-ii/

def find_single(nums):
    if not nums:
        raise Exception("No input was given")

    yoyo1 = 0
    yoyo2 = 0
    for i in nums:
        yoyo2 = yoyo2 | (yoyo1 & i)
        yoyo1 = yoyo1 ^ i

        common_mask = ~(yoyo1 & yoyo2)
        yoyo1 = yoyo1 & common_mask
        yoyo2 = yoyo2 & common_mask

    return yoyo1

assert(find_single([1,1,1,2]) == 2)
assert(find_single([1,1,1,3,3,2,3]) == 2)
