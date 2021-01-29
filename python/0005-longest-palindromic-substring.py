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
    
    
"""
基于区间型动态规划的解法

Time: O(n^2)
Space: O(n^2)
"""

class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        if not s:
            return ""
            
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]
        
        for i in range(n):
            is_palindrome[i][i] = True
        for i in range(1, n):
            is_palindrome[i][i - 1] = True
            
        longest, start, end = 1, 0, 0
        for length in range(1, n):
            for i in range(n - length):
                j = i + length
                is_palindrome[i][j] = s[i] == s[j] and is_palindrome[i + 1][j - 1]
                if is_palindrome[i][j] and length + 1 > longest:
                    longest = length + 1
                    start, end = i, j
                    
        return s[start:end + 1]

            
