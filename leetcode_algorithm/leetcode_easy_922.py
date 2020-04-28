"""
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
"""


"""
version 1 硬做
"""
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even = []
        odd = []
        res = []
        for a in A:
            if a % 2 == 0:
                even.append(a)
            else:
                odd.append(a)
        for i in range(len(even)):
            res.append(even.pop())
            res.append(odd.pop())
        return res

“”“
version 2 sort in place, 略快但思路清奇
”“”
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd, even = [], []
        for i, a in enumerate(A):
            if (i+a)%2 != 0:
                if i % 2 == 0:
                    even.append(i)
                else:
                    odd.append(i)
        for i in range(len(odd)):
            A[odd[i]], A[even[i]] = A[even[i]], A[odd[i]]
        return A