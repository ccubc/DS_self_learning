#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 12:30:37 2019

@author: chengchen

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""

l1 = [1,2,4,5,7,8,10]
l2 = [1,3,4,9]

def solution(l1, l2):
    l3 = []
    while l1 and l2:
        if l1[0]<=l2[0]:
            l3.append(l1.pop(0))
        else: 
            l3.append(l2.pop(0))
    while l1:
        l3.append(l1.pop(0))
    while l2:
        l3.append(l2.pop(0))
    return l3

print(solution(l1,l2))