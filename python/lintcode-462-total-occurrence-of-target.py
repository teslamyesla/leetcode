"""
Time: O(logn)
Space: O(1)
"""

class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def totalOccurrence(self, A, target):
        # write your code here
        """
        Solution 2: Find first occurrence, last occurrence, then calculate distance
        """
        if not A:
            return 0
        
        # find first occurrence
        start, end = 0, len(A) - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if target <= A[mid]:
                end = mid
            else:
                start = mid
                
        if A[start] == target:
            first_match = start
        elif A[end] == target:
            first_match = end
        else:
            return 0 # no match, directly return 0
            
        # find last occurrence
        start, end = 0, len(A) - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if target >= A[mid]:
                start = mid
            else:
                end = mid 
                
        if A[end] == target:
            last_match = end
        elif A[start] == target:
            last_match = start 
        
        return last_match - first_match + 1
        
    """
    My original solution: when target == A[mid], expand from mid
    
    def totalOccurrence(self, A, target):
        # write your code here
        if not A:
            return 0
            
        start, end = 0, len(A) - 1
        count = 0
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if target < A[mid]:
                end = mid
            elif target > A[mid]:
                start = mid
            else: # target == A[mid], expand from mid
                count += 1
                i, j = mid - 1, mid + 1
                
                while i >= 0 and A[i] == target:
                    count += 1
                    i -= 1
                while j < len(A) and A[j] == target:
                    count +=1
                    j += 1
                return count
                
        if A[start] == target or A[end] == target:
            return count + 1
        return 0
    """        
            
