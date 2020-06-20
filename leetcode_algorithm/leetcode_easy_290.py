"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l = s.split()
        len_s = len(pattern)
        if len_s != len(l): return False
        i = 0
        d = {}
        d_word = {}
        while i < len_s:
            if pattern[i] not in d:
                if l[i] not in d_word:
                    d_word[l[i]] = 1
                else: 
                    return False
                d[pattern[i]]=l[i]
            else:
                if d[pattern[i]] != l[i]:
                    return False
            i += 1
        return True