#!/usr/bin/python

import math

def main():
    array = sorted([1,3,6,5,5,7,0,10])
    print(array)

    lower = 0
    upper = len(array)

    to_find = 3
    while lower < upper:
        mid = int(math.floor((lower + upper) / 2))

        mid_val = array[mid]
        print("Testing against %d" % mid_val)
        if mid_val == to_find:
            print("Found it!")
            break

        if mid_val < to_find:
            lower = mid + 1
        else:
            upper = mid
    else:
        print("Did not find it")


if __name__ == "__main__":
    main()
