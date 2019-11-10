#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 16:16:07 2019

@author: chengchen
"""

#%%
def quickSort(x):
    if len(x) <= 1:
        return x
    else:
        pivot = x[0]
        left_list = []
        right_list = []
        for i in x[1:]:
            if i <= pivot:
                left_list.append(i)
            else:
                right_list.append(i)
        return quickSort(left_list)+[pivot]+quickSort(right_list)
print(quickSort([3,1,2,6,2]))


#%% sort in place
def quickSort(x):
    if len(x) <= 1:
        return x
    else:
        pivot = partition(x)
        return quickSort(x[:pivot]) + [x[pivot]] + quickSort(x[pivot+1:])

def partition(x):
    pivot = 0
    right_p = len(x) - 1
    pt = 1
    while pt <= right_p:
        if x[pt]<=x[pivot]:
            x[pt], x[pivot] = x[pivot], x[pt]
            pivot += 1
            pt += 1
        else:
            x[pt], x[right_p] = x[right_p], x[pt]
            right_p -= 1
    return pivot

print(quickSort([3,2,4,1,22,-6,1,4,2,5]))


