"""
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
 

Example 2:

Input: 3
Output: False
"""



from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        d = {}
        for i in range(round(sqrt(c))+1):
            d[(i**2)] = 1
            if (c - i**2) in d:
                return True
        return False