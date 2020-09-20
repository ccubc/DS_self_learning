"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
 

Example 1:

Input: "USA"
Output: True
 

Example 2:

Input: "FlaG"
Output: False
 

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word[0].islower():
            return all(word[i].islower() for i in range(1, len(word)))
        elif len(word) <=2:
            return True
        elif word[1].islower():
            return all(word[i].islower() for i in range(2, len(word)))
        else:
            return all(word[i].isupper() for i in range(2, len(word)))
            