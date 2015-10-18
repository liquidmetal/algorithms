#!/usr/bin/python
import math

def generate_spiral(matrix):
    ret = ""

    m = len(matrix)
    n = len(matrix[0])

    start_row = 0
    end_row = m
    start_col = 0
    end_col = n

    while start_row < end_row and start_col < end_col:
        for i in xrange(start_col, end_col):
            ret += "%s," % (matrix[start_row][i])

        print ret
        start_row += 1

        for i in xrange(start_row, end_row):
            ret += "%s," % (matrix[i][end_col-1])

        print ret
        end_col -= 1

        if start_col < end_col:
            for i in xrange(end_col-1, start_col-1, -1):
                ret += "%s," % (matrix[end_row-1][i])

            print ret
            end_row -= 1

        if start_row < end_row:
            for i in xrange(end_row-1, start_row-1, -1):
                ret += "%s," % (matrix[i][start_col])

            print ret
            start_col += 1

    return ret[:-1]

if __name__ == "__main__":
    m1 = [[1,  2,  3,  4,  5],
          [6,  7,  8,  9,  10],
          [11, 12, 13, 14, 15]]

    out = generate_spiral(m1)
    print(out)
    assert(out == "1,2,3,4,5,10,15,14,13,12,11,6,7,8,9")
