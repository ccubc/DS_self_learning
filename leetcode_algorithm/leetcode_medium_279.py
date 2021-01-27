"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
 

Constraints:

1 <= n <= 104

"""

import math
class Solution:
    def numSquares(self, n: int) -> int:
        if n < 4:
            return n
        lst = [i**2 for i in range(1, round(math.sqrt(n))+1)] # create a list of perfect square numbers that can be used to sum to n
        counter = 0
        current_level = {n} # set
        while len(current_level) > 0:
            counter += 1
            next_level = set() 
            for i in current_level:
                for j in lst:
                    if i < j:
                        break
                    elif i == j:
                        return counter
                    next_level.add(i-j)
                current_level = next_level
        