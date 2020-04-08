"""
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
Note:

The boundaries of each input argument are 1 <= left <= right <= 10000.
"""


def selfDividingNumber(num):
    num_copy = num
    digits = []
    while num > 0:
        digits.append(num%10)
        num = num // 10
    digits = list(set(digits))
    if 0 in digits: return False
    for d in digits:
        if num_copy % d != 0:
            return False
    return True

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right+1):
            if selfDividingNumber(i):
                res.append(i)
        return res