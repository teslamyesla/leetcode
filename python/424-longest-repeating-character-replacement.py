"""
Time: O(n)
Space: O(min(m,n)) where n is length of str, m is char range

Note:
1. counter = collections.Counter(), https://blog.csdn.net/Shiroh_ms08/article/details/52653385
2. Key idea is: Start with a window of size 1 and increase it if size of window (which is hi - lo + 1) minus the amount of occurences of the most frequent character in the window (count) is less than or equal to k.
   https://leetcode.com/problems/longest-repeating-character-replacement/discuss/363071/Simple-Python-two-pointer-solution

"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Intuition: Start with a window of size 1 and increase it if size of window (which is hi - lo + 1) minus the amount of occurences of the most frequent character in the window (count) is less than or equal to k.
        https://leetcode.com/problems/longest-repeating-character-replacement/discuss/363071/Simple-Python-two-pointer-solution
        """
        counter = collections.Counter()
        res, i, max_freq = 0, 0, 0
        for j in range(len(s)):
            counter[s[j]] += 1
            max_freq = max(max_freq, counter[s[j]])
            if j - i + 1 - max_freq > k:
                counter[s[i]] -= 1
                i += 1
            res = max(res, j- i + 1)
        return res
