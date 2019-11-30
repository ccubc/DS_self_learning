#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 15:30:16 2019

@author: chengchen

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
 
"""
nums = [2,19,11,3,7]
target = 9
def twoSum(nums, target):
    """the O(N2) solution"""
    for i in range(len(nums)):
        current = nums[i]
        for j in range(len(nums)-i-1):
            next = nums[i+j+1]
            if current + next == target:
                return ([i, i+j+1])
answer = twoSum(nums, target)
print(answer)

def twoSum2(nums, target):
    """the O(N) solution using dictionary"""
    dic = {}
    for i in range(len(nums)):
        if target - nums[i] not in dic:
            dic[nums[i]] = i
        else:
            return [dic[target - nums[i]], i]
answer = twoSum2(nums, target)
print(answer)
