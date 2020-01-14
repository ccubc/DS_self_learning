#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 13:53:12 2020

SherlockString:
    check if a string contains equal number of letters or can be modified to this pattern by deleting only 1 letter

@author: chengchen
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the isValid function below.
dic = defaultdict(int)
def isValid(s):
    for c in s:
        dic[c]+=1
    l = sorted(list(dic.values()))
    if l[-1] == l[0]:
        return 'YES'
    elif len(l)<=1:
        return 'YES'
    elif l[-2] == l[0] and l[-1] == l[0]+1:
        return 'YES'
    elif l[0]==1 and l[1]==l[-1]:
        return 'YES'
    return 'NO'
    #for key, value in defaultdict:




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
