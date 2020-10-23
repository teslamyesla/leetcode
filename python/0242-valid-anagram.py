"""
Complexity analysis

    Time complexity : O(n). Time complexity is O(n) because accessing the counter table is a constant time operation.
    Space complexity : O(1). Although we do use extra space, the space complexity is O(1) because the table's size stays constant no matter how large n is.

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = {}
        for char in s:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1
                
        for char in t:
            if char not in freq or freq[char] <= 0:
                return False
            freq[char] -= 1
        
        for char in freq.keys():
            if freq[char] != 0:
                return False
    
        return True
    
    """
    1 line solution using sorted(): Time: O(nlogn), Space: O(1)
    
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    """
    
    """
    1 line solution using collections.Counter(): 
    
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)
    """

    
    
