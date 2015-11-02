#!/usr/bin/python

def swap(array, i, j):
    array[i] = array[i] + array[j]
    array[j] = array[i] - array[j]
    array[i] = array[i] - array[j]

def quicksort(array):
    print "Sorting: " + str(array)
    # The end of recursion
    if len(array) <= 1:
        return array

    # Calculate a pivot
    pivot = array[int(len(array) / 2)]
    print("Pivot = %d" % pivot)
    left = 0
    right = len(array) - 1

    while left < right:
        while left <= right:
            if array[left] < pivot:
                left = left + 1
            else:
                break

        while left < right:
            if pivot < array[right]:
                right = right - 1
            else:
                break

        if left < right:
            swap(array, left, right)

    p1 = quicksort(array[:left])
    p2 = quicksort(array[right+1:])

    return p1 + [pivot] + p2

def main():
    array = [6, 8, 10, 45, 12, 90, 23, 13]

    print(array)

    array = quicksort(array)

    print(array)

if __name__ == "__main__":
    main()
