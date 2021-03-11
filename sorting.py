#!/bin/python3

'''
Python provides built-in sort/sorted functions that use timsort internally.
You cannot use these built-in functions anywhere in this file.
'''

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
    s_list = []

    while i < len(xs) and j < len(ys):
        check = cmp(xs[i], ys[j])
        if check == -1:
            s_list.append(xs[i])
            i += 1
        if check == 1:
            s_list.append(ys[j])
            j += 1
        if check == 0:
            s_list.append(xs[i])
            s_list.append(ys[j])
            i += 1
            j += 1

    while i < len(xs):
        s_list.append(xs[i])
        i += 1
    while j < len(ys):
        s_list.append(ys[j])
        j += 1
    return s_list


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
    lo = []
    hi = []
    piv = []

    if len(xs) <= 1:
        return xs
    else:
        value = xs[0]
        for i in xs:
            if i > value:
                hi.append(i)
            elif i < value:
                lo.append(i)
            else:
                piv.append(i)
        less = quick_sorted(lo, cmp=cmp)
        great = quick_sorted(hi, cmp=cmp)

    if cmp == cmp_standard:
        return less + piv + great
    if cmp == cmp_reverse:
        return great + piv + less
