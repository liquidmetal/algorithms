#!/usr/bin/python

# https://www.hackerrank.com/challenges/maxsubarray

import sys

def find_max_contiguous(elements):
    num_elements = len(elements) + 1
    summation = []
    max_val = -sys.maxint -1
    for i in xrange(num_elements):
        summation.append([elements[i]])
        for j in xrange(1, num_elements):
            s = summation[i][j-1] + elements[j]
            summation[i].append(s)

            if s > max_val:
                max_val = s

    return max_val


T = input()
for case in xrange(T):
    num_elements = input()
    elements = [int(x) for x in raw_input().split()]

    sum_contiguous = find_max_contiguous(elements)

    sum_non_contiguous = max(elements)
    non_negative = [x for x in elements if x > 0]
    if non_negative:
        sum_non_contiguous = sum(non_negative)

    print("%s %s" % (sum_contiguous, sum_non_contiguous))
