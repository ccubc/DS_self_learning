#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 22:09:00 2020

@author: chengchen
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    if n <= k:
        c.sort()
        return sum(c[:k])
    else:
        res = 0
        multi = 0
        c.sort(reverse = True)
        for i in range(n):
            if i % k == 0:
                multi += 1
            res += (multi * c[i])
        return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
