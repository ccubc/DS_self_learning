#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:40:47 2019

@author: chengchen

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

def maxProduct(nums):
    curr_max = nums[0]
    all_max = nums[0]
    curr_min = nums[0]
    print(curr_max, curr_min, all_max)
    for i in range(1, len(nums)):
        pre_max = curr_max
        pre_min = curr_min
        curr_max = max(nums[i]*pre_max, nums[i]*pre_min, nums[i])
        curr_min = min(nums[i]*pre_max, nums[i]*pre_min, nums[i])
        all_max = max(all_max, curr_max, curr_min)
        print(all_max, curr_max, curr_min)
    return all_max

nums = [2,-5,-2,-4,3]
print(maxProduct(nums))