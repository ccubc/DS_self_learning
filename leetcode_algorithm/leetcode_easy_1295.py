#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 22:22:57 2020
Given an array nums of integers, return how many of them contain an even number of digits.
 

Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
@author: chengchen
"""

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([(9<i<100 or 999<i<10000) for i in nums])