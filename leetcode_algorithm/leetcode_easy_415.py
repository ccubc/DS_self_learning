#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 14:59:55 2019
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
@author: chengchen
"""
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = list(num1), list(num2)
        carry = 0
        res = []
        while len(num1)>0 or len(num2)>0:
            d1 = ord(num1.pop()) - ord('0') if len(num1) > 0 else 0
            # ord: maps a one-digit str to ASCII code (map to a number)
            # ord('9') - ord('0') will give you 9
            d2 = ord(num2.pop()) - ord('0') if len(num2) > 0 else 0
            temp = d1 + d2 + carry
            res.append(temp % 10)
            carry = temp // 10
        if carry: res.append(carry)
        return ''.join([str(i) for i in res])[::-1]
            # list[::-1] will return the list in reversed order
            # same can be done via: return ''.join([str(i) for i in reversed(res)])
