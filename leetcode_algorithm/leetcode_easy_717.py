#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 10:18:12 2019

We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:
Input: 
bits = [1, 0, 0]
Output: True
Explanation: 
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
Example 2:
Input: 
bits = [1, 1, 1, 0]
Output: False
Explanation: 
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.


@author: chengchen
"""

def isOneBitCharacter(bits):
    i = 0
    j = 0
    while i < (len(bits)):
        if bits[i]==0:
            j = i
            i += 1
        else:
            j = i
            i += 2
    if len(bits) == 0:
        return True
    if j == len(bits)-1:
        return True
    else:
        return False

                
