"""
Time: O(n^2)
Space: O(1)
"""

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        numbers.sort()
        res = []
        
        for smallest_idx in range(len(numbers)-2):
            # dedup
            if smallest_idx != 0 and numbers[smallest_idx] == numbers[smallest_idx - 1]:
                continue
            
            left, right = smallest_idx + 1, len(numbers) - 1
            
            while left < right:
                curr_sum = numbers[smallest_idx] + numbers[left] + numbers[right]
                if curr_sum == 0:
                    res.append([numbers[smallest_idx], numbers[left], numbers[right]])
                    # dedup
                    left += 1
                    right -= 1
                    while left < right and numbers[left] == numbers[left - 1]:
                        left += 1
                    while left < right and numbers[right] == numbers[right + 1]:
                        right -= 1
                elif curr_sum < 0:
                    left += 1
                else:
                    right -= 1
                    
        return res
