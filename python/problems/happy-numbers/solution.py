#!/usr/bin/python

def square(digit):
    d = int(digit)
    return d*d

def happy(num):
    if num == 1:
        return True
    elif num == 4:
        return False

    num = happy(sum(map(square, list(str(num)))))
    return num == 1

print happy(20)
