#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 22:17:12 2020

Hackerrank medium: frequency queries


@author: chengchen
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.

def freqQuery(queries):
    d = defaultdict(int)
    f = defaultdict(int)
    ans = []
    for command, num in queries:
        if command == 1:
            f[d[num]] = max(0, f[d[num]]-1)
            d[num] += 1
            f[d[num]] += 1
        elif command == 2:
            f[d[num]] = max(0, f[d[num]]-1)
            d[num] = max(d[num]-1, 0)
            if d[num] > 0:
               f[d[num]] += 1
        else:
            if f[num]>0:
                ans.append(1)
            else:
                ans.append(0)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
