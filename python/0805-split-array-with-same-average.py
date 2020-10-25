"""

Time Complexity: O(2^{N/2}), where N is the length of A.
Space Complexity: O(2^{N/2}).

"""

class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        """
        Tricks:
        1. sum/n = sum1/k = sum2/(n-k) => only need to enter dfs when satisfying sum*k % n == 0
        2. only need to search half size, one of sum1/sum2 will have less than half of A's size
        3. use memo[(target, size, idx)]: where target-=A[idx], size--, idx++
        4. if len(A) - idx < size: not enough size, return False 
        """
        total, n , memo = sum(A), len(A), {}
        for size in range(1, n//2 + 1):
            if size * total % n == 0 and self.dfs(A, size * total // n, size, 0, memo):
                    return True
        return False
    
    def dfs(self, A, target, size, idx, memo):
        if (target, size, idx) in memo:
            return memo[(target, size, idx)]
        
        if len(A) - idx < size: # not enough element to make up size
            return False
        
        if idx == len(A) or size == 0: # loop to the end
            return target == 0
            
        memo[(target, size, idx)] = self.dfs(A, target - A[idx], size - 1, idx + 1, memo) or \
                                    self.dfs(A, target, size, idx + 1, memo) 
        
        return memo[(target, size, idx)]
