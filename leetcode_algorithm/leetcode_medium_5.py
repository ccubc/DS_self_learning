"""
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        cur_res, longest_res, max_len = "", "", 0
        
        # detect Palindrome with even number of chars e.g. abba
        for i in range(len(s)):
            l,r = i, i+1
            cur_res = ""
            while l >= 0 and r < len(s) and s[l]==s[r]:
                cur_res = s[l] + cur_res + s[r]
                l -= 1
                r += 1
            if len(cur_res) > max_len:
                max_len = len(cur_res)
                longest_res = cur_res

        # detect Palindrome with odd number of chars e.g. abcba
        for i in range(len(s)):
            l, r = i-1, i+1
            cur_res = s[i]
            while l >= 0 and r < len(s) and s[l]==s[r]: # skip the center char
                cur_res = s[l] + cur_res + s[r]
                l -= 1
                r += 1
            if len(cur_res) > max_len:
                max_len = len(cur_res)
                longest_res = cur_res
                
        return longest_res