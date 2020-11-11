"""
Time: O(n)
Space: O(1)

Notes:
1. 先把正负数 partition 开，然后再相向双指针进行交换
2. 当正负数长度不同时，双指针交换起始位置不同
"""

class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
        # write your code here
        """
        先把正负数 partition 开，然后再相向双指针进行交换。
        """
        # partition left to all positive, right to all negative
        left, right = 0, len(A) - 1
        
        while left <= right:
            while left <= right and A[left] > 0:
                left += 1
            while left <= right and A[right] < 0:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        
        num_pos = left
        num_neg = len(A) - left
        
        # exchange with step size = 2    
        # ++---: 0, len(A)-2
        # +++--: 1, len(A)-1
        # ++--:  1, len(A)-2
        if num_neg > num_pos:
            left, right = 0, len(A) - 2
        elif num_neg < num_pos:
            left, right = 1, len(A) - 1
        else: # equal length
            left, right = 1, len(A) - 2
        
        while left < right:
            A[left], A[right] = A[right], A[left]
            left += 2
            right -= 2
            
        return
