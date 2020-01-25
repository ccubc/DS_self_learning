#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 00:28:55 2020
find number of pairs that have a difference equaling k
@author: chengchen
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the pairs function below.
def pairs(k, arr):
    dic = defaultdict(int)
    res = 0
    for i in arr:
        if(i-k in dic):
            res += 1
        if(i+k in dic):
            res += 1
        dic[i]+=1
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
