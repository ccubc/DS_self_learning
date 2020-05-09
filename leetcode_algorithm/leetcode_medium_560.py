#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 09:36:33 2019

@author: chengchen

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
 
"""

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        sums = 0
        d = dict()
        d[0] = 1
        
        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums-k,0)
            d[sums] = d.get(sums,0) + 1
        
        return(count)



# 202005
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        dic = {}
        for n in nums:
            keys = [i+n for i in dic.keys()]
            dic = dict(zip(keys, dic.values()))  
            dic[n] = dic.get(n, 0) + 1
            ans += dic.get(k, 0)
        return ans
    

                




# 201911
def subarraySum(nums, k): # O(N^2)
    dic_pre = {}
    dic_all = {}
    dic_pre[nums[0]] = 1
    dic_all[nums[0]] = 1
    for i in range(1,len(nums)):
        dic_cur = {}
        for j in dic_pre.keys():
            if j + nums[i] not in dic_cur:
                dic_cur[j + nums[i]] = dic_pre[j]
            else:
                dic_cur[j + nums[i]] = dic_pre[j] + 1
                
        if nums[i] not in dic_cur:
            dic_cur[nums[i]] = 1
        else:
            dic_cur[nums[i]] += 1
        for i in dic_cur.keys():
            if i not in dic_all:
                dic_all[i] = dic_cur[i]
            else:
                dic_all[i] += dic_cur[i]
        dic_pre = dic_cur
    if k not in dic_all: 
        return 0
    else:
        return dic_all[k]           
nums = [1,-1,1,-1,1,-1]
k=0
print(subarraySum(nums,k))
