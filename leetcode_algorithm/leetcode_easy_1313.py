#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 13:06:12 2020
Input: nums = [1,2,3,4]
Output: [2,4,4,4]
Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
At the end the concatenation [2] + [4,4,4] is [2,4,4,4].
@author: chengchen
"""

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        pt = 0
        res = []
        while pt < len(nums):
            res += nums[pt]*[nums[pt+1]]
            pt+=2
        return res