"""
Time: O(n^2)
Space: O(1)
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.expandAroundCenter(s, i, i)
            res += self.expandAroundCenter(s, i, i + 1)
        return res
    
    def expandAroundCenter(self, s, l, r):
        if l < 0 or r >= len(s):
            return 0
        cnt = 0
        while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
            cnt += 1
            l -= 1
            r += 1
        return cnt
            

        
