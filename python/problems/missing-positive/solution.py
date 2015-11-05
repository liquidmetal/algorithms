#!/usr/bin/python

def missing_positive(nums):
    # Segregate
    keep_at = 0
    for i in xrange(len(nums)):
        if nums[i] <= 0:
            val = nums[i]
            nums[i] = nums[keep_at]
            nums[keep_at] = val
            keep_at +=  1
 
    positives = nums[keep_at:] 

    if not positives:
        return 1

    for i in positives:
        v = abs(i)-1
        if v < len(positives) and positives[v] > 0:
            positives[v] = -positives[v]

    for i, x in enumerate(positives):
        if x > 0:
            break
    else:
        return i+2

    return i+1

print missing_positive([2,1])
