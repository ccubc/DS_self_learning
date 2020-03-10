#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 22:27:18 2020
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
@author: chengchen
"""

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        ct = Counter(s)
        for i in range(len(s)):
            if ct[s[i]] == 1:
                return i
        return -1
