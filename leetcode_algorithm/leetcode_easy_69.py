#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 17:28:18 2019

@author: chengchen

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
"""
def solution(x):
    if x == 0:
        return 0
    else:
        x_init = x/2
        delta = 1
        x_0 = x_init
        while abs(delta)>0.01:
            x_1 = (x_0+x/x_0)/2
            delta = x_1-x_0
            x_0 = x_1
        return int(x_0)

print(solution(8))