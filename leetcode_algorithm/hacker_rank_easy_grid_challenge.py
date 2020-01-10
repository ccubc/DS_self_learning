#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 12:50:41 2020
gridChallenge
Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending. Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.

For example, given:

a b c
a d e
e f g
The rows are already in alphabetical order. The columns a a e, b d f and c e g are also in alphabetical order, so the answer would be YES. Only elements within the same row can be rearranged. They cannot be moved to a different row.
@author: chengchen
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridChallenge function below.
def gridChallenge(grid):
    # to number
    num = []
    num_row = []   
    res = 'YES'
    for row in grid:
        for x in row:
            num_row.append(ord(x))
        num_row.sort()
        num.append(num_row)
        num_row = []
    print(num)
    print(len(grid[0]))
    print(len(grid)-1)
    for i in range(len(grid)-1):
        for j in range(len(grid[0])):
            print(i)
            print(j)
            if num[i][j] > num[i+1][j]:
                res = 'NO'
                return res
    return res

 

        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
