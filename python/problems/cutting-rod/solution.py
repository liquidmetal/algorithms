#!/usr/bin/python

# Problem: http://www.geeksforgeeks.org/dynamic-programming-set-13-cutting-a-rod/

table = {}
def memoize(func):
    global table
    def wrapper(prices, length):
        h = hash(frozenset(prices))
        if h not in table:
            table[h] = {}

        if length not in table[h]:
            output = func(prices, length)
            table[h][length] = output

        return table[h][length]

    return wrapper

@memoize
def max_price(prices, length):
    """
    prices = the price of the rods
    length = the given length of the rod to cut
    """
    ret = 0
    if length <= 0:
        return 0

    if length == 1:
        return prices[1]


    new_prices = []
    for i in xrange(1, min(len(prices), length+1)):
        new_prices.append( (i, prices[i] + max_price(prices, length-i)) )

    return max([x for (index, x) in new_prices])

def main():
    assert(max_price([0, 1, 5, 8, 9, 10, 17, 17, 20], 8) == 22)
    assert(max_price([0, 3, 5, 8, 9, 10, 17, 17, 20], 8) == 24)

if __name__=='__main__':
    main()
