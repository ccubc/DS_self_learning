#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 13:51:10 2020

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