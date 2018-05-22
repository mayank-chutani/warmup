#!/bin/python3

import sys


def merge(arr, l, m , r):
    inv_count = 0
    n1 = m - l + 1
    n2 = r - m

    l1 = [0] * n1
    l2 = [0] * n2

    for i in range(len(l1)):
        l1[i] = arr[l + i]

    for i in range(len(l2)):
        l2[i] = arr[m + i + 1]

    i = 0
    j = 0
    k = l
    while (i < n1 and j < n2):
        if (l1[i] <= l2[j]):
            arr[k] = l1[i]
            i += 1
        else:
            arr[k] = l2[j]
            j += 1]
            # Numbe of inversions will be (middle index - i), here middle index is n1
            inv_count = inv_count +  (n1-i)
        k += 1

    while (i < n1):
        arr[k] = l1[i]
        k += 1
        i += 1

    while (j < n2):
        arr[k] = l2[j]
        j += 1
        k += 1
    return inv_count

def mergeSort(arr, l, r):
    inv_count = 0
    if (l < r):
        m = l + int((r-l) / 2)
        inv_count = mergeSort(arr, l, m)
        inv_count += mergeSort(arr, m + 1, r)
        inv_count += merge(arr, l, m, r)
    return inv_count

def countInversions(arr):
    inversions = mergeSort(arr, 0, len(arr)-1)
    return inversions


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = countInversions(arr)
        print(result)
