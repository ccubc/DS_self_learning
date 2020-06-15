"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""


# Brute Force, not interesting, O(NlogN)
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        s_nums = sorted(nums)
        print(nums)
        print(s_nums)
        ct = len(nums)
        l = 0
        r = ct-1
        while l<len(nums):
            if nums[l]==s_nums[l]:
                l+=1
                ct-=1
            else:
                break
        if l!=len(nums):
            while r > 0:
                if nums[r] == s_nums[r]:
                    r-=1
                    ct-=1
                else:
                    break
        return ct