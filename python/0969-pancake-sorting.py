"""
Time: O(n^2)
Space: O(n)

leetcode题目和lintcode题目很不同，可以看成相关的两道题目。leetcode flip函数需要自己实现，返回值是开辟额外空间；lintcode是inplace操作。
"""

class Solution:
    """
    @param array: an integer array
    @return: nothing
    """
    
    """
    从左向右遍历，当前未被确定的范围为 [0,len], 确定是最大的且排好序的范围为[len+1,n]
    查询当前范围[0,len]的最大值，其位置为 pos
    通过第一次反转[0,pos], 将范围内最大值放到首部
    通过第二次反转[0,len]，将范维内最大值放到尾部
    未被确定的范围更新为[0,len−1]，重复上面的步骤，保证翻转操作次数最少
    
    Reference: https://www.jiuzhang.com/problem/pancake-sorting/#tag-lang-python
    Reference: https://www.lintcode.com/problem/pancake-sorting/solution
    """
    
    def flip(self, array, idx):
        i = 0 
        while i <= idx // 2:
            array[i], array[idx-i] = array[idx-i], array[i]
            i += 1
        return array
        
    def pancakeSort(self, array):
        n = len(array)
        res = []
        
        for i in range(n - 1, 0, -1):
            max_idx = 0
            for j in range(i + 1):
                if array[j] > array[max_idx]:
                    max_idx = j
                    
            if max_idx != 0 and max_idx != i:
                self.flip(array, max_idx)
                self.flip(array, i)
                res.append(max_idx + 1)
                res.append(i + 1)
            if max_idx == 0:
                self.flip(array, i)
                res.append(i + 1)
        
        return res
        
        
