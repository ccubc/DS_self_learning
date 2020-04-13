"""
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]
 

Example 1:

Input: "IDID"
Output: [0,4,1,3,2]
"""

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        low, high = 0, len(S)
        ans = []
        for c in S:
            if c == "I":
                ans.append(low)
                low += 1
            else:
                ans.append(high)
                high -= 1
        return ans + [low]



import numpy as np
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        level = 0
        level_list = [level]
        mapping = {"I": 1,
                  "D": -1}
        for i, c in enumerate(S):
            level += mapping[c]
            level_list.append(level)
        pos = np.argsort(level_list)
        res = [1]*len(level_list)
        a = 0
        for i in pos:
            res[i] = a
            a += 1
        return res
        