#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 14:48:14 2020

Max Array Sum: return max of sum of subarrays that are consisted of NON-ADJACENT ELEMENTS

@author: chengchen
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum2(arr):
    pre_carry = arr[0] # max sum that includes that last element
    pre_uncarry = 0 # max sum that disincludes that last element
    for i in range(1, len(arr)):
        uncarry = max(pre_carry, pre_uncarry)
        carry = max(arr[i], arr[i] + pre_uncarry)
        pre_carry = carry
        pre_uncarry = uncarry
    return max(carry, uncarry)



def maxSubsetSum(arr):
    if len(arr)>4:
        return maxSubsetSum2(arr)
    else:
        if len(arr) == 4:
            return max(arr[0]+arr[2], arr[1]+arr[3])
        if len(arr) == 3:
            return arr[0] + arr[2]
        else:
            return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
