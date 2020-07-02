"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i, j = 0, len(s)-1
        while i < j:
            while s[i] not in 'aeiouAEIOU' and i < j:
                i+=1
            while s[j] not in 'aeiouAEIOU' and j > i:
                j-=1
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return ''.join(c for c in s)