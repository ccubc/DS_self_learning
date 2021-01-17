"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        # use a dictionary to store the chars on each row
        d = {}
        for i in range(numRows):
            d[i+1]=""
            
        pos, cur_row = 0,1
        fill_down = 1
        while pos < len(s):
            d[cur_row] = d[cur_row] + s[pos]
            cur_row += fill_down
            if cur_row == numRows or cur_row == 1: # if reached the 1st row or last row, change direction
                fill_down *= (-1)
            pos += 1
        res = ""
        for i in range(numRows):
            res = res + d[i+1]
        return res
                    