#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 21:39:49 2020
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.
@author: chengchen
"""

class Solution:
# speed is much faster hahahahaha
    def replaceElements(self, arr: List[int]) -> List[int]:
        pre_m = -1
        for i in range(len(arr)-1, 0, -1):
            cur_m = max(pre_m, arr[i])
            arr[i] = pre_m
            pre_m = cur_m
        arr[0] = pre_m
        return arr    
    
# speed is faster
    def replaceElements(self, arr: List[int]) -> List[int]:
        cur_m = -1
        ans = arr.copy()
        ans[-1] = -1
        for i in range(len(arr)-1, 0, -1):
            cur_m = max(cur_m, arr[i])
            ans[i-1] = cur_m
        return ans    
    
# very slow    
    def replaceElements(self, arr: List[int]) -> List[int]:
        cur_m = -1
        ans = [-1]
        for i in range(len(arr)-1, 0, -1):
            cur_m = max(cur_m, arr[i])
            ans = [cur_m] + ans
        return ans