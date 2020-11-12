"""
Time: O(n)
Space: O(1)
"""

class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        """
        两种类似的思路：
        1.基于老数组新书组傻瓜赋值，非0就赋值进来
        2.基于swap
        
        使用两个指针right和left，left为新数组的指针，right为原数组的指针，原数组指针向后扫，遇到非0的数就赋值给新数组的指针位置，并将新数组指针向后移动
    
        Reference: 
        https://www.jiuzhang.com/problem/move-zeroes/
        https://www.lintcode.com/problem/move-zeroes/solution
        """
        
        """
        Solution 2: 可以保证最小的“写”次数
        
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != 0:
                if right != left:
                    nums[left] = nums[right]
                left += 1
            right += 1
            
        while left < len(nums):
            if nums[left] != 0:
                nums[left] = 0
            left += 1
            
        return nums
        """
        
        """
        Solution 1: 基于swap的版本,无法保证写次数最小,但比较好理解
        
        Two pointers way of writing the code:
        
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
            else:
                right += 1
        return nums
        """
        
        """
        类remove duplicate in array in-place写法：
        """
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1
                
        for i in range(pos, len(nums)):
            nums[i] = 0
            
        return nums
        
                    
        
        
        
