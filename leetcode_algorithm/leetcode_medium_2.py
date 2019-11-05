#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 19:21:43 2019

@author: chengchen

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode(-1)
    current = head
    flag = 0
    while l1 and l2:
        a = l1.val + l2.val + flag
        b = a % 10
        current.next = ListNode(b)
        current = current.next
        l1 = l1.next
        l2 = l2.next
        flag = a//10
    while l1:
        a = l1.val + flag
        b = a % 10
        current.next = ListNode(b)
        current = current.next
        l1 = l1.next
        flag = a//10
    while l2:
        a = l2.val + flag
        b = a % 10
        current.next = ListNode(b)
        current = current.next
        l2 = l2.next
        flag = a//10
    if flag:
        current.next = ListNode(1)
    return head.next

        