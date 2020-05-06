"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
"""



class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            row_dic = {}
            for cell in row:
                if not cell.isdigit(): 
                    continue
                if cell not in row_dic:
                    row_dic[cell] = 1
                else:
                    return False
        for col in range(9):
            col_dic = {}
            for row in range(9):
                if not board[row][col].isdigit():
                    continue
                if board[row][col] not in col_dic:
                    col_dic[board[row][col]] = 1
                else:
                    return False
        for i in range(3):
            for j in range(3):
                cell_dic = {}
                for m in range(3):
                    for n in range(3):
                        cell = board[i*3+m][j*3+n]
                        if cell.isdigit():
                            if cell not in cell_dic:
                                cell_dic[cell] = 1
                            else:
                                return False
        return True
                            
                