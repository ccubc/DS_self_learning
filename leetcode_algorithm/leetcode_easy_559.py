#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 18:37:23 2019

@author: chengchen

Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        if root.children == None:
            return 1
        else: 
            max_d = 1
            for c in root.children:
                cur_d = self.maxDepth(c)
                max_d = max(max_d, cur_d + 1)
            return max_d
