#!/usr/bin/python

# Original question
# https://www.hackerrank.com/challenges/lonely-integer

N = int(raw_input())
nums = [int(x) for x in raw_input().split()]

xor = 0
for num in nums:
    xor = xor ^ num

print(xor)
