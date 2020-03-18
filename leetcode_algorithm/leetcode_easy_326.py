#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 22:51:23 2020
Given an integer, write a function to determine if it is a power of three.
@author: chengchen
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n > 2:
            if n % 3 > 0:
                return False
            return self.isPowerOfThree(n//3)
        if n == 1:
            return True
        else:
            return False