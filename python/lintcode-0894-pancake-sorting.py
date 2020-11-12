"""
Time: O(n)
Space: O(1)

Notes:
1. 思路类似bubble sort, 已排序序列在最后，每次找到未排序序列的最大元素然后先交换到下标0位置，再交换到应在的位置
2. 交换过程中，若最大值不在i处不在0处，则FlipTool.flip(array, max_idx)，FlipTool.flip(array, i)；若在i处，则不用做任何操作；若最大值在0处，只需要做FlipTool.flip(array, i)

"""

class Solution:
    """
    @param array: an integer array
    @return: nothing
    """
    """
    Reference: https://www.lintcode.com/problem/pancake-sorting/solution
    """
    def pancakeSort(self, array):
        n = len(array)
        
        for i in range(n - 1, 0, -1):
            max_idx = 0
            for j in range(i + 1):
                if array[j] > array[max_idx]:
                    max_idx = j
                    
            if max_idx != 0 and max_idx != i:
                FlipTool.flip(array, max_idx)
                FlipTool.flip(array, i)
            if max_idx == 0:
                FlipTool.flip(array, i)
        
        return array
        
    """
    从左向右遍历，当前未被确定的范围为 [0,len], 确定是最大的且排好序的范围为[len+1,n]
    查询当前范围[0,len]的最大值，其位置为 pos
    通过第一次反转[0,pos], 将范围内最大值放到首部
    通过第二次反转[0,len]，将范维内最大值放到尾部
    未被确定的范围更新为[0,len−1]，重复上面的步骤，保证翻转操作次数最少
    时间: O(n)，空间: O(1)
    
    Reference: https://www.jiuzhang.com/problem/pancake-sorting/#tag-lang-python
        
    def pancakeSort(self, array):
        # Write your code here
        
        if not array:
            return 
        
        curr_pos = len(array) - 1
        
        while curr_pos:
            curr_max, max_idx = array[0], 0
            
            for i in range(curr_pos + 1):
                if array[i] > curr_max:
                    curr_max, max_idx = array[i], i
            
            # found max_idx, flip to idx 0
            FlipTool.flip(array, max_idx)
            # then flip to curr_pos
            FlipTool.flip(array, curr_pos)
            
            curr_pos -= 1 
            
        return array
    """
