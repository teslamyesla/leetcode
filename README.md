LeetCode
========

### LeetCode Algorithm &hearts;

### String
| # | Title | Solution | Difficulty | Time | Space | Tag | Legend | Note | Last Submission Date |
|---| ----- | -------- | ---------- | ---- | ----- | --- | ------ | ---- | -------------------- |
|3|[Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Python]()|Medium|O(n)|O(n)|String, Sliding Window|*| One pass: for right in range(len(s)), change left position correspondingly. | 2020-09-02 |
|5|[Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) |[Python]()|Medium|O(n^2)|O(1)|String|*| expandAroundCenter(s,i,i) and expandAroundCenter(s,i,i+1) | 2020-09-01 |
|13|[Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | [Python]()|Easy|O(n)|O(1)|String, Math|y| NA | 2020-09-02 |
|20|[Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | [Python]()|Easy|O(n)|O(n)|String, Stack|y| NA | 2020-09-01 |
|49|[Group Anagrams](https://leetcode.com/problems/group-anagrams/) | [Python]()|Medium| | |String|*|  | 2020-09-03 |
|76|[Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | [Python]()|Hard| | |String, Sliding Window|*|  | 2020-09-03 |
|242|[Valid Anagram](https://leetcode.com/problems/valid-anagram/) | [Python]()|Easy| | |String|y|  | 2020-09-03 |
|424|[Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | [Python]()|Medium|O(n)|O(n)|String, Sliding Window|*| Start with a window of size 1 and increase it if size of window (which is r - l + 1) minus the amount of occurences of the most frequent character in the window (count) is less than or equal to k.| 2020-09-02 |
|680|[Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) | [Python]()|Easy|O(n)|O(1)|String, Two Pointers|*| If s[i] == s[j] then we may take i++; j--. Otherwise, the palindrome must be either s[i+1], s[i+2], ..., s[j] or s[i], s[i+1], ..., s[j-1], and we should check both cases.| 2020-09-01 |




