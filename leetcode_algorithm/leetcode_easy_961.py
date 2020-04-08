"""
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

 

Example 1:

Input: [1,2,3,3]
Output: 3
Example 2:

Input: [2,1,2,5,3,2]
Output: 2
"""

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        d = {}
        for i in A:
            if i not in d:
                d[i] = 1
            else:
                return i