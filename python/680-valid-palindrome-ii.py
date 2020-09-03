"""
Complexity Analysis

    Time Complexity: O(N) where N is the length of the string. Each of two checks of whether some substring is a palindrome is O(N).
    Space Complexity: O(1) additional complexity. Only pointers were stored in memory.
    
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else: 
                # check i:j-1 or i+1:j
                return self.isPalindrome(s[i:j]) or self.isPalindrome(s[i+1:j+1])   
        return True
        
    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
            
        return True
