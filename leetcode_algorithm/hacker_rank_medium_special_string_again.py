#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 21:39:05 2020
A string is said to be a special string if either of two conditions is met:

All of the characters are the same, e.g. aaa.
All characters except the middle one are the same, e.g. aadaa.
A special substring is any substring of a string which meets one of those criteria. Given a string, determine how many special substrings can be formed from it.

For example, given the string s = mnonopoo, we have the following special substrings: {m,n,o,n,o,p,o,o,non,ono,opo,oo}.

Function Description

Complete the substrCount function in the editor below. It should return an integer representing the number of special substrings that can be formed from the given string.

substrCount has the following parameter(s):


@author: chengchen
"""

#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the substrCount function below.
def substrCount(n, s):

    l = [] # list of tuples of continuous occurance of characters
    res = 0
    pre = None # place holder for previous character
    counter = 0  # counts occurance of continuous characters in the tuples

    # 1st pass: create the list of tuples
    for i, c in enumerate(s):
        if c == pre:
            counter += 1
        else:
            if pre is not None:
                l.append((pre, counter))
            pre = c
            counter = 1
    l.append((pre, counter))
    # print (l)

    # 2nd pass: go over the list and add up the continuous situation
    for i in l:
        res += ((i[1]+1)*i[1])//2
    
    # 3rd pass: go over the list and add the scenario with one character in between
    for i in range(len(l)-2):
        if l[i][0] == l[i+2][0] and l[i+1][1]==1:
            res += min(l[i][1], l[i+2][1])

    return res

        
        



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
