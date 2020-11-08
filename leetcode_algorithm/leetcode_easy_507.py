"""
A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise return false.

 

Example 1:

Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.
Example 2:

Input: num = 6
Output: true
"""


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        s = 0
        for i in range(1, ceil(sqrt(num))):
            if num % i == 0:
                s += i
                if i**2 != num:
                    s += (num//i)
        return num == (s - num)
        