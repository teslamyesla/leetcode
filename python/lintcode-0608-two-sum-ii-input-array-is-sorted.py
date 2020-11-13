"""
Time: O(n)
Space: O(1)
"""

class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        i, j = 0, len(nums) - 1
        
        while i < j:
            if nums[i] + nums[j] == target:
                return [i + 1, j + 1]
            if nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1
                
        return [-1, -1]


