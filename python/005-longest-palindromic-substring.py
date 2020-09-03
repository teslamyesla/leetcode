"""
Expand Around Center

Complexity Analysis

    Time complexity : O(n^2). Since expanding a palindrome around its center could take O(n) time, the overall complexity is O(n^2).
    Space complexity : O(1). 
 
Note:
When expandAroundCenter(s, i, i), center is i
When expandAroundCenter(s, i, i + 1), center is between i and i + 1

"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            l1, r1 = self.expandAroundCenter(s, i, i)
            l2, r2 = self.expandAroundCenter(s, i, i + 1)
            if r1-l1 > end-start:
                start, end = l1, r1
            if r2-l2 > end-start:
                start, end = l2, r2
        return s[start:end+1]
            
    def expandAroundCenter(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return l+1, r-1
            
