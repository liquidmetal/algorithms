#!/usr/bin/python

# https://leetcode.com/problems/bulb-switcher/

import math

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """

        return int(math.sqrt(n))

if __name__ == "__main__":
    print Solution().bulbSwitch(100) 
