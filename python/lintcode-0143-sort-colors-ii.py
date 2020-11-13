"""
Time: O(nlogk), where n is the length of numbers, k is the length of colors
Space: O(1)

使用分治法来解决。传入两个区间，一个是颜色区间 color_from, color_to。另外一个是待排序的数组区间 index_from, index_to。
找到颜色区间的中点，将数组范围内进行 partition，<= color 的去左边，>color 的去右边。
然后继续递归。时间复杂度 O(nlogk) n是数的个数， k 是颜色数目。这是基于比较的算法的最优时间复杂度。

"""

class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        
        self.quickSort(colors, 0, len(colors) - 1, 1, k)
        return colors
        
    def quickSort(self, colors, index_from, index_to, color_from, color_to):
        if index_from >= index_to:
            return
        
        if color_from >= color_to:
            return
        
        left, right = index_from, index_to
        pivot = (color_from + color_to) // 2
        
        while left <= right:
            while left <= right and colors[left] <= pivot: # left color <= pivot
                left += 1
            while left <= right and colors[right] > pivot: # right color > pivot
                right -= 1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1
                
        self.quickSort(colors, index_from, right, color_from, pivot)
        self.quickSort(colors, left, index_to, pivot + 1, color_to)
        
        
