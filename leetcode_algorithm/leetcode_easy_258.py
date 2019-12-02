#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 15:59:08 2019

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.

@author: chengchen
"""

def break_digits(num):
    list_digit = []
    while num != 0:
        digit = num % 10
        num = (num-digit)/10
        list_digit.append(digit)
    return list_digit
class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return int(num)
        else:
            list_digit = break_digits(num)
            while len(list_digit) > 1:                
                return self.addDigits(sum(list_digit))
                

# Follow-up: can you do this in O(1) time? without any loop/recursion? 
                
                
