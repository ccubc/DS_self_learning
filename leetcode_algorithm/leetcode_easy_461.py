"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""



class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = list(str(bin(x).replace("0b", "")))
        b = list(str(bin(y).replace("0b", "")))
        if len(b) < len(a):
            a, b = b, a # len(a) <= len(b)
        print(a)
        print(b)
        a = ['0']*(len(b)-len(a)) + a
        ct = 0
        for i in range(len(a)):
            ct += (a[i] != b[i])
        return ct