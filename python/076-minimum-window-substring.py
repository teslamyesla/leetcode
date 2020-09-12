"""
Sliding Window Optimized: Complexity Analysis

    Time Complexity : O(∣S∣+∣T∣) where |S| and |T| represent the lengths of strings S and T. The complexity is same as the previous approach. But in certain cases where ∣filtered_S∣ <<< ∣S∣, the complexity would reduce because the number of iterations would be 2∗∣filtered_S∣+∣T∣.
    Space Complexity : O(∣S∣+∣T∣).
 
Note:
1. target_counter - counter == {}: check all target_counter chars are in counter
2. if s[j] in t: counter[s[j]] += 1; if s[j] not in t, no need to store
3. this problem is similiar with 003. https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        target_counter = collections.Counter(t)
        filter_s = []
        for i in range(len(s)):
            if s[i] in target_counter:
                filter_s.append((i, s[i]))
            
        min_start, min_end, i = -1, len(s), 0
        counter = collections.Counter()
        for j in range(len(filter_s)):
            index_j = filter_s[j][0]
            counter[s[index_j]] += 1
            while target_counter - counter == {}:
            # while all target_counter chars are in counter
                index_i = filter_s[i][0]
                if index_j - index_i < min_end - min_start:
                    min_start, min_end = index_i, index_j
                if counter[s[index_i]] > 1:
                    counter[s[index_i]] -= 1
                else:
                    del counter[s[index_i]]
                i += 1
                
        return s[min_start:min_end + 1] if min_start != -1 else ""        
        
    """
    Sliding Window: Complexity Analysis

    Time Complexity: O(∣S∣+∣T∣) where |S| and |T| represent the lengths of strings S and T. In the worst case we might end up visiting every element of string S twice, once by left pointer and once by right pointer. ∣T∣ represents the length of string T.
    Space Complexity: O(∣S∣+∣T∣). ∣S∣ when the window size is equal to the entire string SSS. ∣T∣ when TTT has all unique characters. 
    
    def minWindow(self, s: str, t: str) -> str:
        min_start, min_end, i = -1, len(s), 0
        counter = collections.Counter()
        target_counter = collections.Counter(t)
        for j in range(len(s)):
            if s[j] in t:
                counter[s[j]] += 1
            while target_counter - counter == {}:
                if j - i < min_end - min_start:
                    min_start, min_end = i, j
                # while all target_counter chars are in counter
                if counter[s[i]] > 1:
                    counter[s[i]] -= 1
                else:
                    del counter[s[i]]
                i += 1
        return s[min_start:min_end + 1] if min_start != -1 else ""
    """
