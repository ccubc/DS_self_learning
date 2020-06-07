"""Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].

"""

class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        row = len(M)
        col = len(M[0])
        ans = [[None for i in range(col)] for j in range(row)]
        for i in range(row):
            for j in range(col):
                ct = 1
                s = M[i][j]
                print(s)                   
                if i-1>=0:
                    s += M[i-1][j]
                    ct+=1
                    if j-1>=0:
                        s += M[i-1][j-1]
                        ct+=1
                    if j+1 < col:
                        s += M[i-1][j+1]
                        ct+=1
                if j-1>=0:
                    s+=M[i][j-1]
                    ct+=1
                if j+1 < col:
                    s+=M[i][j+1]
                    ct+=1
                if i+1 < row:
                    if j-1>=0:
                        s+=M[i+1][j-1]
                        ct+=1
                    s+=M[i+1][j]
                    ct+=1
                    if j+1 < col:
                        s+=M[i+1][j+1]
                        ct+=1

 #               print(f"s {s}  ct{ct}")
                ans[i][j] = s//ct
        return ans