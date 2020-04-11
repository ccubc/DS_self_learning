"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

 

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
"""


# O(N) solution:
from collections import deque
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        l = 0
        r = len(A) - 1
        res = deque()
        while (l <= r):
            if abs(A[l]) < abs(A[r]):
                res.appendleft(A[r]**2)
                r -= 1
            else:
                res.appendleft(A[l]**2)
                l += 1
        return res



# one liner, O(NlogN) solution
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([i**2 for i in A])

