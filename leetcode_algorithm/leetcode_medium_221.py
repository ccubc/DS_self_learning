"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Example 2:
Input: matrix = [["0","1"],["1","0"]]
Output: 1
"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_side_len = 0
        height = len(matrix)
        width = len(matrix[0])
        dp = [[0 for _ in range(width)] for _ in range(height)]
        for i in range(height):
            for j in range(width):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j]) # copy the 1st row and the 1st column
                    max_side_len = max(max_side_len, dp[i][j])
                elif matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    max_side_len = max(max_side_len, dp[i][j])
        return max_side_len**2