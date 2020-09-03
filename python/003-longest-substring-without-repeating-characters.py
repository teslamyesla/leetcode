"""
Complexity Analysis

Sliding Window Solution: 2 pass
    Time complexity : O(2n)=O(n). In the worst case each character will be visited twice by i and j.
    Space complexity : O(min(m,n)). We need O(k) space for the sliding window, where k is the size of the Set. The size of the Set is upper bounded by the size of the string n and the size of the charset/alphabet m.
    
Sliding Window Optimized Solution: 1 pass
    Time complexity : O(n). Index j will iterate n times.
    Space complexity (HashMap) : O(min(m,n)). Same as the previous approach.

Note: 
for r (right) in range(len(s)), change l (left) position correspondingly: 
1) In Sliding window optimized solution: l = max(char_map[s[r]] + 1, l)
2) In Slinding window solution: char_set.remove(s[l]) and l += 1 till s[r] not in char_set

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Solution 2: Sliding Window Optimized
        """
        char_map = {}
        res, l = 0, 0
        for r in range(len(s)):
            if s[r] in char_map:
                l = max(char_map[s[r]] + 1, l)
            char_map[s[r]] = r
            res = max(res, r - l + 1)
        return res        
        
        """
        Solution 1: Sliding Window
        
        char_set = set()
        res, l = 0, 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            res = max(res, r - l + 1)
        return res
        """
