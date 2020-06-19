"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
"""


class Solution:
    def titleToNumber(self, s: str) -> int:
        res, p, l = 0, 0, len(s)
        while p < l:
            res *= 26
            res += (ord(s[p])-64)
            p += 1
        return res
        



class Solution:
    def titleToNumber(self, s: str) -> int:
        d = {}
        for i in range(1,27):
            d[chr(ord('A')-1+i)]=i
        res = 0
        p, l = 0, len(s)
        while p < len(s):
            res *= 26
            res += d[s[p]]
            p += 1
        return res
        