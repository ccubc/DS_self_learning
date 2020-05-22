"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.
"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for i in range(rowIndex+1):
            above = [0] + ans + [0]
            ans = [above[j]+above[j+1] for j in range(i+1)]
        return ans