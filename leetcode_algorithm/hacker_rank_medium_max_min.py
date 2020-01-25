#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 22:23:03 2020

@author: chengchen
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    res = float('inf')
    for i in range(len(arr)-k+1):
        res = min(res, arr[i+k-1]-arr[i])
    print(arr)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
