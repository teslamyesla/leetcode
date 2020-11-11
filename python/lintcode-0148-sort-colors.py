class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        l, r = 0, len(nums) - 1
        i = 0
        # l: first one, r: last non-two
        while i <= r:
            if nums[i] == 0: # 0 throw to l
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1 # if i, l points to the same, move together; else, value = 1, no need to move
            elif nums[i] == 1:
                i += 1
            else: # nums[i] == 2
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
        return nums
                
        
    """
    Solution 2: Two Partitions
    
    def sortColors(self, nums):
        # write your code here
        pos_one = self.partition(nums, 0, len(nums)-1, 0)
        pos_two = self.partition(nums, pos_one, len(nums)-1, 1)
        return nums
    
    def partition(self, nums, start, end, pivot):
        if start >= end:
            return
        
        while start <= end:
            while start <= end and nums[start] <= pivot: # value <= pivot 
                start += 1
            while start <= end and nums[end] > pivot: # value > pivot
                end -= 1
            if start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        return start
    """
        
    """
    Solution 1: Counting Values
    
    def sortColors(self, nums):
        # write your code here
        cnt0, cnt1, cnt2 = 0, 0, 0
        for x in nums:
            if x == 0:
                cnt0 += 1
            elif x == 1:
                cnt1 += 1
            elif x == 2:
                cnt2 += 1
            else:
                raise ValueError
        nums[:cnt0-1] = [0]*cnt0
        nums[cnt0:cnt0+cnt1-1] = [1]*cnt1
        nums[cnt0+cnt1:] = [2]*cnt2
        return nums
    """
