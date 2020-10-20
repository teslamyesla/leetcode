LeetCode
========

### LeetCode Algorithm &hearts;

### String
| # | Title | Difficulty | Time | Space | Tag | Legend | Note | Last Submission Date |
|---| ----- | ---------- | ---- | ----- | --- | ------ | ---- | -------------------- |
|3|[Longest Substring Without Repeating Characters](https://github.com/teslamyesla/leetcode/blob/master/python/003-longest-substring-without-repeating-characters.py) |Medium|O(n)|O(n)|String, Sliding Window|*| One pass: for right in range(len(s)), change left position correspondingly. | 2020-09-02 |
|5|[Longest Palindromic Substring](https://github.com/teslamyesla/leetcode/blob/master/python/005-longest-palindromic-substring.py) |Medium|O(n^2)|O(1)|String|*| expandAroundCenter(s,i,i) and expandAroundCenter(s,i,i+1) | 2020-09-01 |
|13|[Roman to Integer](https://github.com/teslamyesla/leetcode/blob/master/python/013-roman-to-integer.py) |Easy|O(n)|O(1)|String, Math|y| if mapping[s[i]] < mapping[s[i+1]]: res -= mapping[s[i]] | 2020-09-02 |
|20|[Valid Parentheses](https://github.com/teslamyesla/leetcode/blob/master/python/020-valid-parentheses.py) |Easy|O(n)|O(n)|String, Stack|y| NA | 2020-09-01 |
|49|[Group Anagrams](https://github.com/teslamyesla/leetcode/blob/master/python/049-group-anagrams.py) |Medium| O(NK)| O(NK)|String|*| 1. collections.defaultdict(list) - value type is list (default type is int) 2. Use dict[tuple(cnt)].append(s) or dict[''.join(sorted(s))].append(s) - key cannot be list, need to convert to string or tuple| 2020-09-03 |
|76|[Minimum Window Substring](https://github.com/teslamyesla/leetcode/blob/master/python/076-minimum-window-substring.py) |Hard| O(∣S∣+∣T∣) |O(∣S∣+∣T∣) |String, Sliding Window|*| target_counter - counter == {}: check all target_counter chars are in counter; This problem is similiar with 003 | 2020-09-03 |
|125|[Valid Palindrome](https://github.com/teslamyesla/leetcode/blob/master/python/125-valid-palindrome.py) |Easy|O(n)|O(1)|String, Two Pointers|y| s[i].isalpha(), s[i].isdigit(), s[i].lower() | 2020-09-04 |
|242|[Valid Anagram](https://github.com/teslamyesla/leetcode/blob/master/python/242-valid-anagram.py) |Easy|O(n)|O(1)|String|y| Use dict.keys(), collections.Counter() | 2020-09-03 |
|424|[Longest Repeating Character Replacement](https://github.com/teslamyesla/leetcode/blob/master/python/424-longest-repeating-character-replacement.py) |Medium|O(n)|O(n)|String, Sliding Window|*| Start with a window of size 1 and increase it if size of window (which is r - l + 1) minus the amount of occurences of the most frequent character in the window (count) is less than or equal to k.| 2020-09-02 |
|647|[Palindromic Substrings](https://github.com/teslamyesla/leetcode/blob/master/python/647-palindromic-substrings.py) |Medium|O(n^2)|O(1)|String|y| Same as 005, expandAroundCenter(s,i,i) and expandAroundCenter(s,i,i+1) | 2020-09-04 |
|680|[Valid Palindrome II](https://github.com/teslamyesla/leetcode/blob/master/python/680-valid-palindrome-ii.py) | Easy|O(n)|O(1)|String, Two Pointers|*| If s[i] == s[j] then we may take i++; j--. Otherwise, the palindrome must be either s[i+1], s[i+2], ..., s[j] or s[i], s[i+1], ..., s[j-1], and we should check both cases.| 2020-09-01 |


### Dynamic Programming
| # | Title | Difficulty | Time | Space | Tag | Legend | Note | Last Submission Date |
|---| ----- | ---------- | ---- | ----- | --- | ------ | ---- | -------------------- |
|416|[Partition Equal Subset Sum](https://github.com/teslamyesla/leetcode/blob/master/python/416-partition-equal-subset-sum.py) |Medium|O(m⋅n)|O(m)|DP, DFS, memo|*| 1. Convert to subSetSum = sum // 2  2. Similiar as Coin Change DP, but each number can only be used once (thus DP[i] update in a reverse order) | 2020-10-18 |
|473|[Matchsticks to Square](https://github.com/teslamyesla/leetcode/blob/master/python/473-matchsticks-to-square.py) |Medium|O(4^n)|O(n)|DFS, memo, backtracking|*| for i in range(4): sums[i] += nums[idx]; dfs; sums[i] -= nums[idx] | 2020-10-19 |

