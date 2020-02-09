#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 12:31:18 2020
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

@author: chengchen
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        record = [] # list to store sum of elements on the same level and the level
        def dfs(node, depth = 0):
            if node:  # <=> if node is not None
                if len(record) <= depth:
                    record.append([0,0]) # sum of elements, and level
                record[depth][0] += node.val
                record[depth][1] += 1
                dfs(node.left, depth + 1)
                dfs(node.right, depth +1)
        dfs(root)
        return [s/c for s, c in record]