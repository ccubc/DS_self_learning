#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 13:33:50 2019

@author: chengchen

LeetCode 914. (easy)

In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.
Example 1:

Input: [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]
Example 2:

Input: [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.
Example 3:

Input: [1]
Output: false
Explanation: No possible partition.
Example 4:

Input: [1,1]
Output: true
Explanation: Possible partition [1,1]
Example 5:

Input: [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2]

Note:

1 <= deck.length <= 10000
0 <= deck[i] < 10000
"""


deck = [1,1,1,1,2,2,2,2,2,2]
def gcd(a,b): # get common divider of two integers
    a, b = (a, b) if a>=b else (b, a)
    while b:
        a, b = b, a%b
    return a
def gcd_multi(list_number): # get common divider from a list of number
    while len(list_number)>1:
        a = list_number.pop()
        b = list_number.pop()
        c = gcd(a,b)
        list_number.append(c)
    return list_number.pop()
def solution(deck):
    dictionary = {x:deck.count(x) for x in deck}
    dictionary_values = list(dictionary.values())
    unique_d_value = list(set(dictionary_values))
    unique_d_value.sort(reverse=True)
    if unique_d_value[-1]==1: # deck contains unique value card
        return False
    else:
        if len(unique_d_value) == 1:
            return True
        else:
            gcd = gcd_multi(unique_d_value)
            return (gcd>1)
print(solution(deck))



# improved version using counter
from collections import Counter
def solution2(deck):
    c = Counter(deck)
    l = list(c.values())
    k = l[0]
    for i in range(1,len(l)):
        k = gcd(k, l[i])
    if(k>1):
        return True
    else:
        return False
print(solution2(deck))

# the second method uses less time and the code looks cleaner!
    
