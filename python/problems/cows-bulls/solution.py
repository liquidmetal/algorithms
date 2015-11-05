#!/usr/bin/python

# https://leetcode.com/problems/bulls-and-cows/

class Solution(object):
    def getHint(self, secret, guess):
        num_cows = 0
        num_bulls = 0

        has_digits = []

        for i in xrange(len(secret)):
            if secret[i] == guess[i]:
                num_bulls += 1

                # Make it unavailable
                secret = secret[:i] + '-' + secret[i+2:]
            else:
                if secret[i] in guess:
                    num_cows += 1


        return "%dA%dB" % (num_bulls, num_cows)
