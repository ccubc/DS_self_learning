
def transform(word):
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    res = []
    a = ord('a')
    for c in list(word):
        res.append(morse[ord(c)-a])
    return ''.join(res)

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        return len(set(list(map(transform, words))))

