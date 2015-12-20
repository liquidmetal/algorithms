#!/usr/bin/python

import sys
import numpy as np

s = "actwtcac"
num_chars = len(s)

dp = np.zeros( (num_chars, num_chars) )

# O(n)
for i in xrange(len(s)):        # 0, 1, 2, 3.. len(s)-1
    for j in xrange(i+1):       # O(n)
        # i-1 -> the previous center
        # j+1 -> 
        if( ((i-j) <= 2 or dp[i-1][j+1]==1) and s[i] == s[j]):
            dp[i][j] = 1
            print("%s for (%d, %d)" % (s[j:i+1], i, j))

print(dp)
