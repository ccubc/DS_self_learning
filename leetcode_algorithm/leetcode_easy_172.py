"""
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
"""

class Solution:
    def trailingZeroes(self, n: int) -> int:
        m = 5
        delta = n//m
        res = 0
        while delta > 0:
            res += delta
            m *= 5
            delta = n//m
        return res
