"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        ans = []
        ctr = 0
        for word in strs:
            sorted_wd = ''.join(sorted(list(word)))
            if sorted_wd not in dic:
                dic[sorted_wd] = ctr
                ctr += 1
                ans.append([word])
            else:
                ans[dic[sorted_wd]].append(word)
        return ans
            