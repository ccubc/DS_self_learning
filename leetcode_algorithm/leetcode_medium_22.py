"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8

"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.dfs(n, n, ans, "")
        return ans
    
        
    def dfs(self, left, right, ans, string):
        if left > right:
            return
        if left == 0 and right == 0:
            ans.append(string)
            return
        if left > 0:
            self.dfs(left-1, right, ans, string+"(")
        if right > 0:
            self.dfs(left, right-1, ans, string+")")
        