#!/usr/bin/python

def two_sum(nums, e):
    nums = sorted(nums)

    i = 0
    j = len(nums) - 1
    results = []
    while i < j and i<len(nums) and j>=0:
        val = nums[i] + nums[j]
        if val < e:
            i += 1
        elif val > e:
            j -= 1
        else:
            results.append( (nums[i], nums[j]) )
            i += 1
            j -= 1

            while nums[i] == nums[i-1]:
                i += 1

            while nums[j] == nums[j+1]:
                j -= 1

    return results

print two_sum([5, 9, 0, -5, -4], 0)
print two_sum([5, 4, 0, -5, -4], 0)
