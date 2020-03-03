#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 20:48:53 2020

@author: chengchen
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        while i < len(s)-i-1:
            s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]
            i += 1
        return s