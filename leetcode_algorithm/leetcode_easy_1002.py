Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]


""" Second attempt with Counter but with same logic """
from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if len(A) == 0:
            return []
        c1 = Counter(A[0])
        for i in range(1, len(A)):
            c2 = Counter(A[i])
            c1 = c1 & c2
        return list(c1.elements())
            


""" Initial ugly trial"""
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if len(A) == 0:
            return []
        dic1 = dict(zip(list('abcdefghijklmnopqrstuvwxyz'), [0]*26))
        for c in list(A[0]):
            dic1[c]+=1
        pre = list(dic1.values())
        for i in range(1, len(A)):
            dic2 = dict(zip(list('abcdefghijklmnopqrstuvwxyz'), [0]*26))
            for c in list(A[i]):
                dic2[c]+=1
            after = list(dic2.values())
            pre = [min(pre[i], after[i]) for i in range(26)]
        dic = dict(zip(list('abcdefghijklmnopqrstuvwxyz'), pre))
        ans = []
        for key, value in dic.items():
            if value > 0:
                ans.extend([key]*value)
        return ans