"""
Time: O(nlogk)
Space: O(k)
"""

import heapq

class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        heap = []
        
        for i in range(len(nums)):
            if i < k:
                heapq.heappush(heap, nums[i])
            else:
                heapq.heappush(heap, nums[i])
                heapq.heappop(heap)
                
        return sorted(heap, reverse = True)
