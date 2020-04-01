class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        for row in grid:
            i = 0
            while i < len(row) and row[i] >= 0:
                i += 1
            res += (len(row) - i)
        return res


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid[0])
        for row in grid:
            i = 0
            for i in range(n):
                if row[i] < 0:
                    res += (n - i)
                    break
        return res