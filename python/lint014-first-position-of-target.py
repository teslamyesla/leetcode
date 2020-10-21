"""
Time: O(logn)
Space: O(1)
"""

class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        if not nums:
            return -1
            
        start, end = 0, len(nums) - 1 
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if target <= nums[mid]:
                end = mid
            else:
                start = mid
                
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
            
        return -1
