#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 16:16:04 2020

Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

Given a str, find number of substring pairs that are anagrams


@author: chengchen
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    l = 1
    ls = len(s)
    dic = {}
    while l < ls:
        for i in range(ls-l+1):
            x = list(s[i:i+l])
            x.sort()
            y = "".join(x)
            if y not in dic:
                dic[y] = 1
            else:
                dic[y] += 1
        l += 1
    c = 0
    for k in dic.keys():
        v = dic[k]
        c += (v*(v-1)/2)
    return int(c)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
