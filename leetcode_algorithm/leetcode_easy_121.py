#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 20:59:57 2019

@author: chengchen

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

def maxProfit(prices):
    if (len(prices)==0):
        return 0
    else:
        min_price = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            if prices[i]< min_price:
                min_price = prices[i]
            if prices[i]-min_price > max_profit:
                max_profit = prices[i]-min_price
        return max_profit

print(maxProfit([7,6,4,3,1]))
print(maxProfit([7,1,5,3,6,4]))