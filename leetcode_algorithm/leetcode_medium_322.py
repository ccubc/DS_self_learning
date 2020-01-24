#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 14:26:43 2020

@author: chengchen
"""

# Recursion --- Time Limit Surpassed

class Solution:
    def findN(self, coins: List[int], amount: int) -> int:
        min_n_change = float('inf')
        for i in coins:
            if i == amount:
                found = True
                return 1
            if amount > i:
                min_n_change = min(1 + self.findN(coins, amount - i), min_n_change)
        return min_n_change
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        n = self.findN(coins, amount)
        if n > 99999999:
            return -1
        else:
            return n
        

# Dynamic Programming
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Dynamic Programming
        coins.sort()
        c = coins[0]
        res = []
        for a in range(amount + 1):
            if a%c == 0:
                res.append(a//c)
            else:
                res.append(float('inf'))
        del(coins[0])
        for c in coins:
            for a in range(c, amount+1):
                prev = res[a]
                res[a] = min(res[a-c]+1, prev)
        if res[-1] == float('inf'):
            return -1
        else:
            return res[-1]
                
                

            