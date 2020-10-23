"""
Complexity analysis:

    Time complexity : O(n) because we simply traverse the given string one character at a time and push and pop operations on a stack take O(1) time.
    Space complexity : O(n) as we push all opening brackets onto the stack and in the worst case, we will end up pushing all the brackets onto the stack. e.g. ((((((((((.
    
"""

class Solution:
    def isValid(self, s: str) -> bool:
        # corner case
        if not s:
            return True
        
        mapping = {')':'(', ']':'[', '}':'{'}
        left_chars = set(['(','[','{'])
        right_chars = set([')',']','}'])
        
        stack = []
        for char in s:
            if char in left_chars:
                stack.append(char)
            else:
                if not stack:
                    return False
                pop_char = stack.pop()
                if pop_char != mapping[char]:
                    return False
        
        return not stack

    
    
