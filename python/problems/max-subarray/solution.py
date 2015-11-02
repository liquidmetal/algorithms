#!/usr/bin/python

# https://www.hackerrank.com/challenges/maxsubarray

import sys

def find_max_contiguous(elements):
    num_elements = len(elements)
    summation = []
    max_val = max(elements)
    for i in xrange(num_elements):
        if i > 0:
            summation.append([0] * i)
            summation[i].append(elements[i])
        else:
            summation.append([elements[i]])


        for j in xrange(i+1, num_elements):
            s = summation[i][j-1] + elements[j]
            summation[i].append(s)

            if s > max_val:
                max_val = s

    print summation

    return max_val


# Sample input
# 1
# 6
# 10 20 30 40 -50 -60

T = input()
for case in xrange(T):
    num_elements = input()
    elements = [int(x) for x in raw_input().split()]

    sum_contiguous = find_max_contiguous(elements)

    import pdb; pdb.set_trace()
    sum_non_contiguous = max(elements)
    non_negative = [x for x in elements if x > 0]
    if non_negative:
        sum_non_contiguous = sum(non_negative)

    print("%s %s" % (sum_contiguous, sum_non_contiguous))
