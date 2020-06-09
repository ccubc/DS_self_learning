"""
We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
"""


class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) < 2:
            return A == B
        for i in range(len(A)):
            A = A[1:] + A[0]
            if A == B:
                return True
        return False