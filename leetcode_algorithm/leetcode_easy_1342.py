#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 13:51:10 2020
Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

 
@author: chengchen
"""

class Solution:
    def numberOfSteps (self, num: int) -> int:
        counter = 0
        while num > 0:
            if num % 2 == 0:
                counter += 1
                num = num/2
            else:
                counter += 1
                num -= 1
        return counter