#!/usr/bin/python

# https://leetcode.com/problems/product-of-array-except-self/

class Solution(object):
    def productExceptSelf(self, nums):
        ret = []
        n = len(nums)

        # Pass from left
        for i in xrange(n):
            if i > 0:
                ret.append(ret[-1] * nums[i-1]);
            else:
                ret.append(1)

        tmp = 1
        for i in xrange(n-1, -1, -1):
            if i < n-1:
                tmp = tmp * nums[i+1]
            ret[i] = ret[i] * tmp

        return ret

if __name__ == "__main__":
    print Solution().productExceptSelf([1,2,3,4])
    print Solution().productExceptSelf([])
    print Solution().productExceptSelf([1])
    print Solution().productExceptSelf([0, 1, 2])
