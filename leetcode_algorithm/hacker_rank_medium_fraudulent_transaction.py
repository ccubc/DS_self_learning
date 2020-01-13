#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 15:50:08 2020

@author: chengchen
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.

""" Fast solution using Python bisect
bisect --- array bisection algorithm: maintain a list in sorted order without having to sort the list after each insertion.
"""
from bisect import insort, bisect_left
def activityNotifications(expenditure, d):
    t = sorted(expenditure[:d]) # original list of transactions in d consecutive days
    res = 0
    for i, current in enumerate(expenditure[d:]):
        if d % 2 == 0: # d is even
            if current >= t[d//2-1] + t[d//2]:
                res += 1
        else: # d is odd
            if current >= 2 * (t[d//2]):
                res += 1
        drop_index = bisect_left(t, expenditure[i]) 
        # if we were to insert expenditure[i] in the sorted array t, the index that it will be inserted
        del(t[drop_index]) # drop the element in the sorted array
        insort(t, current)
    return res



""" Brute Force Solution """
def median(l):
    l.sort()
    ll = len(l)
    if ll%2 == 0:
        return (l[int(ll//2)-1]+l[int(ll//2)]/2)
    else:
        return l[int(ll//2)]

def activityNotifications2(expenditure, d):
    counter = 0
    for i in range(d,len(expenditure)):
        if expenditure[i] >= 2*median(expenditure[i-d:i]):
            counter += 1
    return counter



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
