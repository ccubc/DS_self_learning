"""
Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

If no land or water exists in the grid, return -1.

 

Example 1:



Input: [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: 
The cell (1, 1) is as far as possible from all the land with distance 2.
Example 2:



Input: [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: 
The cell (2, 2) is as far as possible from all the land with distance 4.
 

Note:

1 <= grid.length == grid[0].length <= 100
grid[i][j] is 0 or 1
"""


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n_visited = 0
        l = len(grid)
        n_total = l*l
        base = 0
        bfs = []
        for i in range(l):
            for j in range(l):
                if grid[i][j] == 1:
                    bfs.append([i,j])
                    n_visited += 1
        if n_visited in [0,n_total]: 
            return -1
        while n_visited < n_total:
            new_bfs = []
            base += 1
            for pos in bfs:
                if pos[0]>0:
                    if grid[pos[0]-1][pos[1]] != 1:
                        grid[pos[0]-1][pos[1]] = 1
                        n_visited+=1
                        new_bfs.append([pos[0]-1, pos[1]])
                if pos[0]<l-1:
                    if grid[pos[0]+1][pos[1]] != 1:
                        grid[pos[0]+1][pos[1]] = 1
                        n_visited+=1
                        new_bfs.append([pos[0]+1, pos[1]])
                if pos[1]>0:
                    if grid[pos[0]][pos[1]-1] != 1:
                        grid[pos[0]][pos[1]-1] = 1
                        n_visited+=1
                        new_bfs.append([pos[0],pos[1]-1])
                if pos[1]<l-1:
                    if grid[pos[0]][pos[1]+1] != 1:
                        grid[pos[0]][pos[1]+1] = 1
                        n_visited+=1
                        new_bfs.append([pos[0],pos[1]+1])                        
            bfs = new_bfs
        return base

            
                
                
            