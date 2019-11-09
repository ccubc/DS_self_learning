#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 21:10:31 2019

@author: chengchen

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

"""

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        current = head
        prev = None
        while current != None:
            next_ = current.next
            current.next = prev
            prev = current
            current = next_
        return prev
         
