"""
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
 

Note:

The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
"""

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # look for zeros' positions
        nrow = len(matrix)
        ncol = len(matrix[0])
        total = nrow * ncol
        pos = []
        target = 0
        ctr = 0
        total = nrow*ncol
        ans = [[-1 for i in range(ncol)] for j in range(nrow)]
        for i in range(nrow):
            for j in range(ncol):
                if matrix[i][j] == 0:
                    pos.append([i,j])
                    ans[i][j] = 0
                    ctr += 1
        # while matrix is not filled:
        # wrap target with (target + 1)
        # target += 1
        while ctr < total:
            ans, pos, ctr = wrap(ans, target, pos, ctr)
            target += 1
        return ans
def wrap(ans, target, pos, ctr):
    nrow = len(ans)
    ncol = len(ans[0])
    pos_new = []
    for p in pos:
        if 0<p[0]<nrow and -1<p[1]<ncol:
            if ans[p[0]-1][p[1]] < 0:
                ans[p[0]-1][p[1]] = target + 1
                pos_new.append([p[0]-1, p[1]])
                ctr+=1
        if -1<p[0]<nrow-1 and -1<p[1]<ncol:
            if ans[p[0]+1][p[1]] < 0:
                ans[p[0]+1][p[1]] = target + 1
                pos_new.append([p[0]+1, p[1]])
                ctr += 1
        if -1<p[0]<nrow and 0<p[1]<ncol:
            if ans[p[0]][p[1]-1] < 0:
                ans[p[0]][p[1]-1] = target + 1
                pos_new.append([p[0], p[1]-1])
                ctr += 1
        if -1<p[0]<nrow and -1<p[1]<ncol-1:
            if ans[p[0]][p[1]+1] < 0:
                ans[p[0]][p[1]+1] = target + 1
                pos_new.append([p[0], p[1]+1])
                ctr+=1
    return ans, pos_new, ctr

