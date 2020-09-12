"""
Complexity Analysis

    Time Complexity: O(NK), where N is the length of strs, and K is the maximum length of a string in strs. Counting each string is linear in the size of the string, and we count every string.
    Space Complexity: O(NK), the total information content stored in ans.

"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Solution 2: Categorize by Count
        
        defaultdict reference: https://stackoverflow.com/questions/5900578/how-does-collections-defaultdict-work
        """
        dict = collections.defaultdict(list)
        for s in strs:
            cnt = [0] * 26
            for char in s:
                cnt[ord(char) - ord('a')] += 1
            dict[tuple(cnt)].append(s)
        return dict.values()
        
    """
    Solution 1: Categorized by Sorted String
    
    Complexity Analysis

    Time Complexity: O(NKlog⁡K), where N is the length of strs, and K is the maximum length of a string in strs. The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(Klog⁡K) time.
    Space Complexity: O(NK), the total information content stored in ans. 
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in dict:
                dict[sorted_s] = [s]
            else:
                dict[sorted_s].append(s)
        return dict.values()
    """
