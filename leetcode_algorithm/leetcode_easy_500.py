"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
 

Note:

You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        d = {'q':1, 'w':1, 'e':1, 'r':1, 't':1, 'y':1, 'u':1, 'i':1, 'o':1, 'p':1,
            'a':100, 's':100, 'd':100, 'f':100, 'g':100, 'h':100, 'j':100, 'k':100, 'l':100,
            'z':-1, 'x':-1, 'c':-1, 'v':-1, 'b':-1, 'n':-1, 'm':-1}
        res = []
        for i, word in enumerate(words):
            s = sum([d[c] for c in word.lower()])
            l = len(word)
            if s in [l, 100*l, -1*l]:
                res.append(word)
        return res