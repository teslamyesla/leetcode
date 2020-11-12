"""
Time: O(n)
Space: O(1)

Python解法会原地assign char in str，是无效解法，会报错！
"""

class Solution:
    """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """
    def sortLetters(self, chars):
        # write your code here
        """
        This problem does not have a good answer for python. 
        Python strings are immutable (i.e. they can't be modified)
        You'll get error message: str' object does not support item assignment
        """
        left, right = 0, len(chars) - 1
        
        while left <= right:
            while left <= right and 'a' <= chars[left] <= 'z':
                left += 1
            while left <= right and 'A' <= chars[right] <= 'Z':
                right -= 1
            if left <= right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
                
        return

