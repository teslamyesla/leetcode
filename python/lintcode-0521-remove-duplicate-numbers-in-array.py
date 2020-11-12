"""
Extra Space Solution:
Time: O(n)
Space: O(n)

In Place Solution:
Time: O(nlogn)
Space: O(1)

"""

class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        """
        Solution 1: O(n) time with extra space
        
        i = 0
        for x in set(nums):
            nums[i] = x
            i += 1
        return i
        """
        
        """
        Solution 2: O(nlogn) time without extra space
        """
        if not nums:
            return 0
            
        nums.sort()
        pos = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[pos] = nums[i]
                pos += 1
                
        return pos
        
        """
        Two pointers way of writing the code:
        
        if not nums:
            return 0
            
        nums.sort()
        left, right = 1, 1
        while right < len(nums):
            if right != 0 and nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
                right += 1
            else:
                right += 1
        return left
        """
        
        
        
