LeetCode
========

### LeetCode Algorithm "&hearts;"

### String
| # | Title | Solution | Difficulty | Time | Space | Tag | Legend | Note |
|---| ----- | -------- | ---------- | ---- | ----- | --- | ------ | ---- |
|3|[Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Python]()|Medium|O(n)|O(n)|String,Sliding Window|*| Right 1 pass: for r in range(len(s)), change l position correspondingly. |
|5|[Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) |[Python]()|Medium|O(n^2)|O(1)|String|*| expandAroundCenter(s,i,i) and expandAroundCenter(s,i,i+1) |
|13|[Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | [Python]()|Easy|O(n)|O(1)|String,Math|*| |
|20|[Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | [Python]()|Easy|O(n)|O(n)|String,Stack|y| |
|424|[Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | [Python]()|Medium|O(n)|O(n)|String,Sliding Window|*| Start with a window of size 1 and increase it if size of window (which is r - l + 1) minus the amount of occurences of the most frequent character in the window (count) is less than or equal to k.|
|680|[Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) | [Python]()|Easy|O(n)|O(1)|String,Two Pointers|*| If s[i] == s[j] then we may take i++; j--. Otherwise, the palindrome must be either s[i+1], s[i+2], ..., s[j] or s[i], s[i+1], ..., s[j-1], and we should check both cases.|




