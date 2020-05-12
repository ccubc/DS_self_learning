"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

"""


class Solution:
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        r = m+n-1
        r1 = m-1
        r2 = n-1
        while r1 >= 0 and r2 >= 0:
            if nums1[r1] >= nums2[r2]:
                nums1[r], nums1[r1] = nums1[r1], nums1[r]
                r1 -= 1
            else:
                nums1[r] = nums2[r2]
                r2 -= 1
            r -= 1
        if r1 < 0:
            for i in range(r + 1):
                nums1[i] = nums2[i]
        return nums1