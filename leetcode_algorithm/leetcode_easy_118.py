"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 1:
            return []
        else:
            ans = [[1]]
            for i in range(2, numRows+1):
                above = [0] + ans[i-2] + [0] # the above row
                row = [above[j] + above[j+1] for j in range(i)]
                ans.append(row)
        return ans