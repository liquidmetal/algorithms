#!/usr/bin/python

# https://leetcode.com/problems/4sum/

def four_sum(nums, e):
    nums = sorted(nums)
    results = []

    checked_i = []
    checked = []

    for i in xrange(len(nums)-3):
        if nums[i] in checked_i:
            continue

        checked_i.append(nums[i])
        checked = []
        for j in xrange(i+1, len(nums)-2):
            if nums[j] in checked:
                continue

            checked.append(nums[j])
            k = j + 1
            l = len(nums) - 1

            while k < l:
                summation = nums[i] + nums[j] + nums[k] + nums[l]
                if summation > e:
                    l -= 1
                elif summation < e:
                    k += 1
                else:
                    results.append( (nums[i], nums[j], nums[k], nums[l]) )
                    print (i, j, k, l)
                    print (nums[i], nums[j], nums[k], nums[l])

                    l -= 1
                    k += 1

                    while nums[k] == nums[k-1]:
                        k += 1
                        if k == len(nums):
                            break

                    while nums[l] == nums[l+1]:
                        l -= 1
                        if l == 0:
                            break

    return results

#print four_sum([-3,-2,-1,0,0,1,2,3], 0)
print four_sum([-1,-5,-5,-3,2,5,0,4], -7)
