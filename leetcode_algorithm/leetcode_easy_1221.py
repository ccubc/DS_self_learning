#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 18:04:57 2020

@author: chengchen
"""

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        dic = {'R':1, 'L':-1}
        counter = 0
        total = 0
        for c in s:
            total += dic[c]
            if total == 0:
                counter += 1
        return counter
        
        