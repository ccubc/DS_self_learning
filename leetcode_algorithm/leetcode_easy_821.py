"""
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
"""


def left_scan(S, C):
    found = False
    left_scan_distance = []
    for c in S:
        if c == C:
            found = True
            counter = 0
            left_scan_distance.append(0)
        elif found == False:
            left_scan_distance.append(float("inf"))
        else:
            counter += 1
            left_scan_distance.append(counter)
    return left_scan_distance

class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        # scan from left to right:
        left = left_scan(S,C)
        right = left_scan(S[::-1], C)[::-1]
        ans = [min(left[i], right[i]) for i in range(len(S))]
        return ans