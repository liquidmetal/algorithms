#!/usr/bin/python

# https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution(object):
    def maxProduct(self, words):
        masks = []
        for word in words:
            masks.append(self.get_word_char_mask(word))

        max_length = 0
        for i, w1 in enumerate(words):
            for j, w2 in enumerate(words):
                if (masks[i] & masks[j]) > 0:
                    continue

                new_len = len(w1) * len(w2)
                if new_len > max_length:
                    max_length = new_len

        return max_length


    def get_word_char_mask(self, word):
        ret = 0
        base = ord('a')
        for ch in word:
            ret = ret | (1 << (ord(ch)-base))

        return ret

if __name__ == "__main__":
    print Solution().maxProduct(["a", "aa", "aaa", "aaaa"])
    print Solution().maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"])
    print Solution().maxProduct([])
