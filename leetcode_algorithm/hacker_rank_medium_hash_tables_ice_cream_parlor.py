#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 22:45:16 2020

@author: chengchen
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    dic = defaultdict(int)
    for i, c in enumerate(cost):
        if dic[money - c] > 0:
            print('{} {}'.format(dic[money-c], i+1))
        else:
            dic[c] = i+1

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
