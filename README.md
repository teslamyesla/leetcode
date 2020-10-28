LeetCode
========

### LeetCode Algorithm &hearts;

### String
| # | Title | Difficulty | Time | Space | Tag | Legend | Note | Last Submission Date |
|---| ----- | ---------- | ---- | ----- | --- | ------ | ---- | -------------------- |
|3|[Longest Substring Without Repeating Characters](https://github.com/teslamyesla/leetcode/blob/master/python/0003-longest-substring-without-repeating-characters.py) |Medium|O(n)|O(n)|String, Sliding Window|*| One pass: for right in range(len(s)), change left position correspondingly. | 2020-09-02 |
|5|[Longest Palindromic Substring](https://github.com/teslamyesla/leetcode/blob/master/python/0005-longest-palindromic-substring.py) |Medium|O(n^2)|O(1)|String|*| expandAroundCenter(s,i,i) and expandAroundCenter(s,i,i+1) | 2020-09-01 |
|13|[Roman to Integer](https://github.com/teslamyesla/leetcode/blob/master/python/0013-roman-to-integer.py) |Easy|O(n)|O(1)|String, Math|y| if mapping[s[i]] < mapping[s[i+1]]: res -= mapping[s[i]] | 2020-09-02 |
|20|[Valid Parentheses](https://github.com/teslamyesla/leetcode/blob/master/python/0020-valid-parentheses.py) |Easy|O(n)|O(n)|String, Stack|y| NA | 2020-09-01 |
|49|[Group Anagrams](https://github.com/teslamyesla/leetcode/blob/master/python/0049-group-anagrams.py) |Medium| O(nK), n: # of strs, K: maxlen of str in strs| O(nK)|String|*| 1. collections.defaultdict(list) - value type is list (default type is int) 2. Use dict[tuple(cnt)].append(s) or dict[''.join(sorted(s))].append(s) - key cannot be list, need to convert to string or tuple| 2020-09-03 |
|76|[Minimum Window Substring](https://github.com/teslamyesla/leetcode/blob/master/python/0076-minimum-window-substring.py) |Hard| O(∣S∣+∣T∣), len of str S & T |O(∣S∣+∣T∣) |String, Sliding Window|*| target_counter - counter == {}: check all target_counter chars are in counter; This problem is similiar with 003 | 2020-09-03 |
|125|[Valid Palindrome](https://github.com/teslamyesla/leetcode/blob/master/python/0125-valid-palindrome.py) |Easy|O(n)|O(1)|String, Two Pointers|y| s[i].isalpha(), s[i].isdigit(), s[i].lower() | 2020-09-04 |
|242|[Valid Anagram](https://github.com/teslamyesla/leetcode/blob/master/python/0242-valid-anagram.py) |Easy|O(n)|O(1)|String|y| Use dict.keys(), collections.Counter() | 2020-09-03 |
|424|[Longest Repeating Character Replacement](https://github.com/teslamyesla/leetcode/blob/master/python/0424-longest-repeating-character-replacement.py) |Medium|O(n)|O(n)|String, Sliding Window|*| Start with a window of size 1 and increase it if size of window (which is r - l + 1) minus the amount of occurences of the most frequent character in the window (count) is less than or equal to k.| 2020-09-02 |
|647|[Palindromic Substrings](https://github.com/teslamyesla/leetcode/blob/master/python/0647-palindromic-substrings.py) |Medium|O(n^2)|O(1)|String|y| Same as 005, expandAroundCenter(s,i,i) and expandAroundCenter(s,i,i+1) | 2020-09-04 |
|680|[Valid Palindrome II](https://github.com/teslamyesla/leetcode/blob/master/python/0680-valid-palindrome-ii.py) | Easy|O(n)|O(1)|String, Two Pointers|*| If s[i] == s[j] then we may take i++; j--. Otherwise, the palindrome must be either s[i+1], s[i+2], ..., s[j] or s[i], s[i+1], ..., s[j-1], and we should check both cases.| 2020-09-01 |


### Dynamic Programming
| # | Title | Difficulty | Time | Space | Tag | Legend | Note | Last Submission Date |
|---| ----- | ---------- | ---- | ----- | --- | ------ | ---- | -------------------- |
|322|[Coin Change](https://github.com/teslamyesla/leetcode/blob/master/python/0322-coin-change.py) |Medium|O(S*n), S: amount, n: number of coins|O(S)|DP|*| F[i] = min(F[i], F[i-coin] + 1) for coin in coins | 2020-10-20 |
|416|[Partition Equal Subset Sum](https://github.com/teslamyesla/leetcode/blob/master/python/0416-partition-equal-subset-sum.py) |Medium|O(m⋅n), m: amount, n: number of elements|O(m)|DP, DFS, memo|*| 1. Convert to subSetSum = sum // 2  2. Similiar as Coin Change DP, but each number can only be used once (thus DP[i] update in a reverse order) | 2020-10-18 |
|473|[Matchsticks to Square](https://github.com/teslamyesla/leetcode/blob/master/python/0473-matchsticks-to-square.py) |Medium|O(4^n)|O(n)|DFS, memo, backtracking|*| for i in range(4): sums[i] += nums[idx]; dfs; sums[i] -= nums[idx] | 2020-10-19 |
|494|[Target Sum](https://github.com/teslamyesla/leetcode/blob/master/python/0494-target-sum.py) |Medium|O(l*n), l: range of sum, n: number of elements|O(l*n)|DFS, memo|*| memo[(target, idx)] = dfs(idx+1, target-nums[idx]) + dfs(idx+1, target+nums[idx]) | 2020-10-22 |
|518|[Coin Change 2](https://github.com/teslamyesla/leetcode/blob/master/python/0518-coin-change-2.py) |Medium|O(S*n), S: amount, n: number of coins|O(n)|DP|*| if i == coin: F[i] += 1; else F[i] += F[i-coin] for coin in coins | 2020-10-21 |
|805|[Split Array With Same Average](https://github.com/teslamyesla/leetcode/blob/master/python/0805-split-array-with-same-average.py) |Hard|O(2^(n/2))|O(2^(n/2))|DP|*| Key trick is sum/n = sum1/k = sum2/(n-k) => only need to enter dfs when satisfying sum * k % n == 0! | 2020-10-24 |
|956|[Tallest Billboard](https://github.com/teslamyesla/leetcode/blob/master/python/0956-tallest-billboard.py) |Hard|O(n*s)|O(n*s)|DP, DFS, memo|*| Really hard problem with a lot of tricks both in DP and DFS solution! see py file for details | 2020-10-25 |
|1049|[Last Stone Weight II](https://github.com/teslamyesla/leetcode/blob/master/python/1049-last-stone-weight-ii.py) |Medium|O(m⋅n), m: sum(stones)//2, n: number of stones|O(m)|DP|*| 1. Key trick is to transform problem to find target cloest to sum(stones) // 2; 2. dp[i] stores max amount achievable that <= i | 2020-10-23 |

LintCode
========

### LintCode only algorithm &hearts;

### Binary Search
| # | Title | Difficulty | Time | Space | Tag | Legend | Note | Last Submission Date |
|---| ----- | ---------- | ---- | ----- | --- | ------ | ---- | -------------------- |
|14|[First Position of Target](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-014-first-position-of-target.py) |Easy|O(logn)|O(1)|Binary Search|y| NA | 2020-10-20 |
|458|[Last Position of Target](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-458-last-position-of-target.py) |Easy|O(logn)|O(1)|Binary Search|y| NA | 2020-10-20 |
|462|[Total Occurrence of Target](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-462-total-occurrence-of-target.py) |Easy|O(logn)|O(1)|Binary Search|y| NA | 2020-10-20 |


### Graph
| # | Title | Difficulty | Time | Space | Tag | Legend | Note | Last Submission Date |
|---| ----- | ---------- | ---- | ----- | --- | ------ | ---- | -------------------- |
|178|[Graph Valid Tree](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-178-graph-valid-tree.py) |Medium| O(n)| O(n)|DFS / Union Find|*| 3 properties of tree: 1) connectivity 2) n-1 edges for n node tree 3) no cycle. Satisfy any 2 of above qualifies for a tree. DFS checks 1+2, Union Find checks 2+3 | 2020-10-14 |
|431|[Connected Component in Undirected Graph](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-431-connected-component-in-undirected-graph.py) |Medium| O(V+E) | O(V) | DFS / Union Find|*| NA | 2020-10-14 |
|892|[Alien Dictionary](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-892-alien-dictionary.py) |Hard| O(V+E)=O(n*k), n: # of words, k: avg word length| O(V+E)=O(n*k)|Topology Sort|*| 1. char is the node, char to char relationship is the dependency, use topology sort 2. use HEAP instead of Queue to maintain lexicographical order during topological sort! | 2020-10-14 |

