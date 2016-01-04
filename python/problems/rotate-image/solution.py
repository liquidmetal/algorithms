#!/usr/bin/python

import math, pprint

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for y in range(int(math.floor(n/2))):
            for x in range(y, n-y-1):
                tmp = matrix[y][x]
                matrix[y][x] = matrix[n-x-1][y]
                matrix[n-x-1][y] =matrix[n-y-1][n-x-1]
                matrix[n-y-1][n-x-1] = matrix[x][n-y-1]
                matrix[x][n-y-1] = tmp

        # Reverse and swap
        """
        for y in range(n):
            for x in range(n/2):
                tmp = matrix[y][x]
                matrix[y][x] = matrix[y][n-x-1]
                matrix[y][n-x-1] = tmp

        for y in range(n-1):
            for x in range(n-y):
                tmp = matrix[y][x]
                matrix[y][x] = matrix[n-x-1][n-y-1]
                matrix[n-x-1][n-y-1] = tmp
        """

        return 

def print_matrix(matrix):
    for y in xrange(len(matrix)):
        for x in xrange(len(matrix)):
            print(matrix[y][x]),

        print ""

if __name__ == "__main__":
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]];
    #matrix = [[1,2,3], [4,5,6], [7,8,9]]
    #matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    print("Earlier")
    print_matrix(matrix)
    Solution().rotate(matrix)
    print
    print("Rotated")
    print_matrix(matrix)
