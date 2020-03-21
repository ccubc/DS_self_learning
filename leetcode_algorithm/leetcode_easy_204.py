#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 22:19:18 2020
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
@author: chengchen
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, n):
        # faster solution: for i in range(2, int(n**0.5)+1):
            if primes[i]:
                primes[i*i:n:i] = [False]*len(primes[i*i:n:i])
        return sum(primes)        
            