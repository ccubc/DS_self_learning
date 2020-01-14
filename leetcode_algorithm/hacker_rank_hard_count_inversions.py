#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:17:07 2020

Count inversions: In an array, if i<j and arr[i]>arr[j], we say that arr[i] and arr[j] are inverted
We can fix an inversion by swapping adjacent elements. 
Write a function to count # times of inversions needed to be done to be able to sort arrays.

@author: chengchen
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.


"""
Merge Sort O(NlogN)
"""


def merge(arr, left, right):
    inversion = 0
    i = 0 # pointer to the left half
    j = 0 # pointer to the right half
    k = 0 # pointer to the array
    left_length = len(left)
    right_length = len(right)
    while i < left_length and j < right_length: # when there are elements left in both left and right half of the arrays
        if left[i] <= right[j]: # no inversion needed
            arr[k] = left[i]
            i += 1
        else: # inversion needed
            arr[k] = right[j]
            j += 1
            inversion += (left_length - i)
        k += 1
    while i < left_length: 
        arr[k] = left[i]
        i+=1
        k+=1
    while j < right_length:
        arr[k] = right[j]
        j+=1
        k+=1
    return inversion

def merge_sort(arr):
    if len(arr) <= 1:
        return 0
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    inversion = merge_sort(left) + merge_sort(right) + merge(arr, left, right)
    return inversion

# Complete the countInversions function below.
def countInversions(arr):
    return merge_sort(arr)



def countInversions2(arr):
"""
bubble sort, O(N2)
"""
    l = len(arr)
    counter = 0
    for i in range(l):
        for j in range(l-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                counter += 1
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()

