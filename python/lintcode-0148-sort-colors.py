"""
Time: O(n)
Space: O(1)

3种解法！

"""

class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    
    """
    Solution 3: Two Pointers One Pass
    Reference: https://www.jiuzhang.com/problem/sort-colors/#tag-lang-python
    
    我们建立首尾双指针left和right，分别指示0/1边界和1/2边界。left左边（不含left）全为0，right右边（不含right）全为2。初始化left和mid为0，right 为len(nums)-1。
    第三个指针mid从left起向right移动，边扫描边实时更新两个边界。
        若 nums[mid]为 0 ：交换第 mid个和第left个元素，并将 left 指针和mid指针都向右移。
        若 nums[mid]为 2 ：交换第 mid个和第 right个元素，并将 right指针左移
        若 nums[mid]为 1 ：将指针mid右移。
    注意：当mid与left交换后，mid能够后移; 而mid与right交换后，mid要重新处理！！！ 因为mid左边交换来的是处理过的数字，而mid右边交换来的是未经处理的数字，要重新处理。
    具体mid左边从left交换过来的只会是0（当mid和left指针重合时，此时交换和不交换无区别，两个指针一同++就可以）或1（当mid和left指针不重合是，left指针指向的是处理过的数字，而又非0，所以是1，换到mid也是无须再次处理，直接++）
    """
    def sortColors(self, nums):
        left, mid, right = 0, 0, len(nums) - 1
        
        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1 # move to the next number
            elif nums[mid] == 2:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
            else: # nums[mid] == 1
                mid += 1
                
        return nums
        
    """
    Solution 2: Two Partitions
    与普通partition不同之处：
    普通partition: while nums[left] < pivot, left += 1, 
                   while nums[right] > pivot, right -= 1
    两边都不包含等于pivot的情况, 要换的位置是nums[left] <= pivot, nums[right] >= pivot, 换完后分布是 <= pivot, pivot, >= pivot
    而此处例如pivot = 1时，我们不想得到 <= 1, 1, >= 1这样的分布，因为左右两边依然混杂着0, 1或1，2
    我们想要得到的是 < 1, 1, >= 1这样的分布，因此交换的条件是左边>= pivot, 右边< pivot, 交换完满足左边< pivot, 右边>= pivot
    
    def sortColors(self, nums):
        pos_1 = self.partition(nums, 0, len(nums) - 1, 1)
        pos_2 = self.partition(nums, pos_1, len(nums) - 1, 2)
        return nums
        
    def partition(self, nums, start, end, pivot):
        if start >= end:
            return
        
        left, right = start, end 
        
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] >= pivot: # pay attention to the >= here!!
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        # start, right, pivot, left, end  
        return left
    """
    
    """
    Solution 1: Counting Values
    
    def sortColors(self, nums):
        # write your code here
        count_0, count_1, count_2 = 0, 0, 0
        for num in nums:
            if num == 0:
                count_0 += 1
            elif num == 1:
                count_1 += 1
            elif num == 2:
                count_2 += 1
            else:
                continue
            
        nums[:count_0] = [0] * count_0
        nums[count_0:count_0 + count_1] = [1] * count_1
        nums[count_0 + count_1:] = [2] * count_2
        
        return nums
    """
    
    
