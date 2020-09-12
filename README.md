LeetCode
========

### LeetCode Algorithm &hearts;

### String
| # | Title | Solution | Difficulty | Time | Space | Tag | Legend | Note | Last Submission Date |
|---| ----- | -------- | ---------- | ---- | ----- | --- | ------ | ---- | -------------------- |
|3|[Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [003-longest-substring-without-repeating-characters.py](https://github.com/teslamyesla/leetcode/blob/master/python/003-longest-substring-without-repeating-characters.py)|Medium|O(n)|O(n)|String, Sliding Window|*| One pass: for right in range(len(s)), change left position correspondingly. | 2020-09-02 |
|5|[Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) |[005-longest-palindromic-substring.py](https://github.com/teslamyesla/leetcode/blob/master/python/005-longest-palindromic-substring.py)|Medium|O(n^2)|O(1)|String|*| expandAroundCenter(s,i,i) and expandAroundCenter(s,i,i+1) | 2020-09-01 |
|13|[Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | [013-roman-to-integer.py](https://github.com/teslamyesla/leetcode/blob/master/python/013-roman-to-integer.py)|Easy|O(n)|O(1)|String, Math|y| if mapping[s[i]] < mapping[s[i+1]]: res -= mapping[s[i]] | 2020-09-02 |
|20|[Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | [020-valid-parentheses.py](https://github.com/teslamyesla/leetcode/blob/master/python/020-valid-parentheses.py)|Easy|O(n)|O(n)|String, Stack|y| NA | 2020-09-01 |
|49|[Group Anagrams](https://leetcode.com/problems/group-anagrams/) | [Python]()|Medium| | |String|*|  | 2020-09-03 |
|76|[Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | [Python]()|Hard| | |String, Sliding Window|*|  | 2020-09-03 |
|242|[Valid Anagram](https://leetcode.com/problems/valid-anagram/) | [242-valid-anagram.py](https://github.com/teslamyesla/leetcode/blob/master/python/242-valid-anagram.py)|Easy|O(n)|O(1)|String|y| dict.keys(), collections.Counter() | 2020-09-03 |
|424|[Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | [424-longest-repeating-character-replacement.py](https://github.com/teslamyesla/leetcode/blob/master/python/424-longest-repeating-character-replacement.py)|Medium|O(n)|O(n)|String, Sliding Window|*| Start with a window of size 1 and increase it if size of window (which is r - l + 1) minus the amount of occurences of the most frequent character in the window (count) is less than or equal to k.| 2020-09-02 |
|680|[Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) | [680-valid-palindrome-ii.py](https://github.com/teslamyesla/leetcode/blob/master/python/680-valid-palindrome-ii.py)|Easy|O(n)|O(1)|String, Two Pointers|*| If s[i] == s[j] then we may take i++; j--. Otherwise, the palindrome must be either s[i+1], s[i+2], ..., s[j] or s[i], s[i+1], ..., s[j-1], and we should check both cases.| 2020-09-01 |




