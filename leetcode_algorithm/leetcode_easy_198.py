#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 22:00:54 2020
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
@author: chengchen
"""

# 20210120 revisit
class Solution:
    def rob(self, nums: List[int]) -> int:
        nums = [0] + nums
        dp = nums
        for i in range(2, len(dp)):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        return dp[-1]


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        pre = 0 # biggest sum not including current
        cur = nums[0] # biggest sum that includes the current
        for i, n in enumerate(nums):
            if i == 0:
                continue
            new_pre = max(cur, pre)
            cur = n + pre
            pre = new_pre
        return max(pre, cur)
            