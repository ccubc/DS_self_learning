"""
Given an integer n. Each number from 1 to n is grouped according to the sum of its digits. 

Return how many groups have the largest size.

 

Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. There are 4 groups with largest size.
Example 2:

Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.
Example 3:

Input: n = 15
Output: 6
Example 4:

Input: n = 24
Output: 5
"""

def get_digits(i):
    res = []
    while i > 9:
        res.append(i%10)
        i = i//10
    res.append(i)
    return res
class Solution:
    def countLargestGroup(self, n: int) -> int:
        dic = {}
        for i in range(1, n+1):
            digits = get_digits(i)
            sum_digits = sum(digits)
            if sum_digits not in dic:
                dic[sum_digits] = 1
            else:
                dic[sum_digits] += 1
        max_size = max(dic.values())
        counter = 0
        for i in dic.values():
            if i == max_size:
                counter += 1
        return counter