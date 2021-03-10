#!/bin/python3

'''
Python provides built-in sort/sorted functions that use timsort internally.
You cannot use these built-in functions anywhere in this file.
'''

import random
from copy import deepcopy


def cmp_standard(a, b):
    '''
    used for sorting from lowest to highest


    >>> cmp_standard(125, 322)
    -1
    >>> cmp_standard(523, 322)
    1
    '''

    if a < b:
        return -1
    if b < a:
        return 1
    return 0


def cmp_reverse(a, b):
    '''
    used for sorting from highest to lowest

    >>> cmp_reverse(125, 322)
    1
    >>> cmp_reverse(523, 322)
    -1
    '''
    if a < b:
        return 1
    if b < a:
        return -1
    return 0


def cmp_last_digit(a, b):
    '''
    used for sorting based on the last digit only

    >>> cmp_last_digit(125, 322)
    1
    >>> cmp_last_digit(523, 322)
    1
    '''
    return cmp_standard(a % 10, b % 10)


def _merged(xs, ys, cmp=cmp_standard):
    '''
    >>> _merged([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    '''
    i = j = 0
    xsys = []

    while i < len(xs) and j < len(ys):
        check = cmp(xs[i], ys[j])
        if check == -1:
            xsys.append(xs[i])
            i += 1
        if check == 1:
            xsys.append(ys[j])
            j += 1
        if check == 0:
            xsys.append(xs[i])
            xsys.append(ys[j])
            i += 1
            j += 1

    while i < len(xs):
        xsys.append(xs[i])
        i += 1

    while j < len(ys):
        xsys.append(ys[j])
        j += 1

    return xsys


def merge_sorted(xs, cmp=cmp_standard):
    '''
    Merge sort is the standard O(n log n) sorting algorithm.
    Recall that the merge sort pseudo code is:

        if xs has 1 element
        it is sorted, so return xs
        else
            divide the list into two halves left,right
            sort the left
            sort the right
            merge the two sorted halves

    You should return a sorted version of the input list xs.
    You should not modify the input list xs in any way.
    '''
    xs_copy = deepcopy(xs)
    if len(xs_copy) <= 1:
        return xs_copy
    else:
        mid = len(xs_copy) // 2
        left = xs_copy[0:mid]
        right = xs_copy[mid:]
        lef = merge_sorted(left, cmp)
        ri = merge_sorted(right, cmp)
        return _merged(lef, ri, cmp)


def quick_sorted(xs, cmp=cmp_standard):
    xs_copy = deepcopy(xs)
    if len(xs_copy) <= 1:
        return xs_copy
    else:
        piv = random.randrange(len(xs_copy))
        low = xs_copy[0:piv]
        hi = xs_copy[piv:]
        return _merged((merge_sorted(low, cmp), merge_sorted(hi, cmp)), cmp)
