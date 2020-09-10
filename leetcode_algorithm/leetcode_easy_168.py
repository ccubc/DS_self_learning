"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
"""
class Solution:
    def convertToTitle(self, n: int) -> str:
        d = {}
        for i in range(1,27):
            d[i] = chr(ord('A')+i-1)
        res = []
        while n > 0:
            if n % 26 > 0:
                res = [d[n%26]]+res
                n = (n-n%26)/26
            else:
                res = ['Z']+res
                n = (n-26)//26
        return ''.join(res)