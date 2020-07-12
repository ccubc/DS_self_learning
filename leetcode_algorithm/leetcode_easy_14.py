"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        ans = ""
        i = 0
        while i < len(strs[0]):
            c = strs[0][i]
            for word in strs[1:]:
                if len(word) <= i or word[i] != c:
                    return ans
            ans = ans + c
            i += 1
        return ans