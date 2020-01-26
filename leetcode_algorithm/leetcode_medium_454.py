#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 00:27:46 2020
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2
@author: chengchen
"""

from collections import defaultdict
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        def cal2Sum(l1, l2):
            dic = defaultdict(int)
            for i in l1:
                for j in l2:
                    dic[i+j] += 1
            return dic
        dic1 = cal2Sum(A, B)
        dic2 = cal2Sum(C, D)
        res = 0
        for key, value in dic2.items():
            res += dic1[-key]*value
        return res
                    
#another solution using Counter, but with similar idea
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        countSumAB = collections.Counter(a+b for a in A for b in B)
        return sum(countSumAB[-c-d] for c in C for d in D)