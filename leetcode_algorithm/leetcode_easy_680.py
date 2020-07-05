"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        i,j = 0, len(s)-1
        while i < j:
            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                return self.checkPalindrome(s[i+1:j+1]) or self.checkPalindrome(s[i:j])
        return True
    
    
    def checkPalindrome(self, s):
        i, j = 0, len(s)-1
        while i < j:
            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                return False
        return True
            