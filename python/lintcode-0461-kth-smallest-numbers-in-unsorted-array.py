"""
Time: O(n)
Space: O(1)

Notes:
1. 经典Quick Select算法题。Quick Select算法的主要目的是在一个没有排序的数组里面，找到第k小的元素。
2. if start >= end: return nums[k]
3. 注意最后的边界条件: if right >= k; if left <= k; else

"""

class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        # write your code here
        """
        Quick Select: http://www.noteanddata.com/classic-algorithm-quick-select.html
        Quick Select算法的主要目的是在一个没有排序的数组里面，找到第k小的元素。
        Quick select算法和quick sort算法都是由Tony Hoare（图灵奖获得者）发明的。 基本思路也是非常类似的，都是通过分治的思想，把整个大问题转化成小问题来求解。

        Reference: https://www.lintcode.com/problem/kth-smallest-numbers-in-unsorted-array/solution
        """
        return self.quickSelect(nums, 0, len(nums) - 1, k - 1)
        
    def quickSelect(self, nums, start, end, k):
        if start >= end:
            return nums[k]
            
        left, right = start, end
        pivot = nums[(left + right) // 2]
        
        while left <= right:
            while left <= right and nums[left] < pivot: # when equal to pivot, still need to exchange
                left += 1
            while left <= right and nums[right] > pivot: # when equal to pivot, still need to exchange
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        # [start, right] [left, end]
        if right >= k:
            return self.quickSelect(nums, start, right, k)
        if left <= k:
            return self.quickSelect(nums, left, end, k)
        return nums[k]
        
