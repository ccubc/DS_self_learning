#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 23:11:37 2020
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
@author: chengchen
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        s = 0
        for i in nums:
            if i not in d:
                d[i] = 1
                s += i
            else:
                del d[i]
                s -= i
        return s