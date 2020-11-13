"""
Solution 1: Use Quick Select
Time: O(n)
Space: O(1)

Solution 2: Use Min Heap
Time: O(n)
Space: O(k)

"""

class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    """
    Solution 2: Use Min Heap
    """
    def kthLargestElement(self, n, nums):
        import heapq
        
        heap = [] 
        
        for i in range(len(nums)):
            if i < n: # push
                heapq.heappush(heap, nums[i])
            else: # push then pop
                heapq.heappush(heap, nums[i])
                heapq.heappop(heap)
                
        return heap[0]
        
    
    """
    Solution 1: Use Quick Select
    
    def kthLargestElement(self, n, nums):
        # write your code here
        return self.quickSelect(nums, 0, len(nums) - 1, n - 1)
        
    def quickSelect(self, nums, start, end, k):
        if start >= end:
            return nums[k]
            
        left, right = start, end
        pivot = nums[(left + right) // 2]
        
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        # [start, right] pivot [left, end]
        if right >= k:
            return self.quickSelect(nums, start, right, k)
        if left <= k:
            return self.quickSelect(nums, left, end, k)
        return nums[k]
    """
