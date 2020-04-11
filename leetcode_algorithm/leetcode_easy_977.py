"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

 

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
"""


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([i**2 for i in A])