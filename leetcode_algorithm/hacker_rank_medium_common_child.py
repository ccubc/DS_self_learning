#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 21:10:14 2020

@author: chengchen
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    # dynamic programming
    l = len(s1)+1
    res = [[0 for col in range(l)] for row in range(l)]
    for i in range(1,l):
        for j in range(1,l):
            if s1[i-1] == s2[j-1]:
                res[i][j] = res[i-1][j-1]+1
            else:
                res[i][j] = max(res[i-1][j], res[i][j-1])
    return res[-1][-1]





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
