#!/usr/bin/python

# https://leetcode.com/problems/3sum/

def three_sum(nums, e):
    nums = sorted(nums)
    result = []

    for i in xrange(len(nums)-2):
        j = i+1
        k = len(nums) - 1

        while j < k:
            if nums[i] + nums[j] + nums[k] < e:
                j += 1
            elif nums[i] + nums[j] + nums[k] > e:
                k -= 1
            else:
                result.append( (nums[i], nums[j], nums[k]) )

                j += 1
                k -= 1

                # Skip duplicates
                while nums[j] == nums[j-1]:
                    j += 1

                while nums[k] == nums[k+1]:
                    k -= 1

    return result


print three_sum([-1,0,1,2,-1,-4], 0)
