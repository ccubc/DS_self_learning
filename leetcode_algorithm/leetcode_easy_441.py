#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:26:51 2020
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.
@author: chengchen
"""

class Solution:
    def arrangeCoins(self, n: int) -> int:
        res = 0
        needed = 0
        while True:
            res += 1
            needed += res
            if needed > n:
                return (res-1)
            