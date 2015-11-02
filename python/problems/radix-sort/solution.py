#!/usr/bin/python

import math

def main():
    array = [6,5,188, 490, 235, 109]

    m = 10
    n = 1
    max_length = len(array)
    done = False
    while not done:
        buckets = {}
        for num in array:
            b = int( (num%m) / n)
            if b not in buckets:
                buckets[b] = []

            buckets[b].append(num)

            array = []
            for b in buckets.keys():
                array.extend(buckets[b])
                if len(buckets[b]) == max_length:
                    done = True

        m = m * 10
        n = n * 10

    print(array)

if __name__ == "__main__":
    main()
