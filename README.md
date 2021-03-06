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
|969|[Pancake Sorting](https://github.com/teslamyesla/leetcode/blob/master/python/0969-pancake-sorting.py) |Medium|O(n^2)|O(n)|Bubble Sort|*| Idea similiar as bubble sort, leetcode problem is different from lintcode one, thus provide both solutions | 2020-11-04 |


### Dynamic Programming
| # | Title | Difficulty | Time | Space | Tag | Legend | Note | Last Submission Date |
|---| ----- | ---------- | ---- | ----- | --- | ------ | ---- | -------------------- |
|198|[House Robber](https://github.com/teslamyesla/leetcode/blob/master/python/0198-house-robber.py) |Easy|O(n)|O(n)|DP|*| NA | 2020-11-02 |
|322|[Coin Change](https://github.com/teslamyesla/leetcode/blob/master/python/0322-coin-change.py) |Medium|O(S*n), S: amount, n: number of coins|O(S)|DP|*| F[i] = min(F[i], F[i-coin] + 1) for coin in coins | 2020-10-20 |
|375|[Guess Number Higher or Lower II](https://github.com/teslamyesla/leetcode/blob/master/python/0375-guess-number-higher-or-lower-ii.py) |Medium|O(n^3)|O(n^2)|DP, DFS, memo|*| memo[(start, end)], for x in the range, if guessing x you need to pay x + max(helper(start,x-1),helper(x+1,end)), take min cost | 2020-10-28 |
|416|[Partition Equal Subset Sum](https://github.com/teslamyesla/leetcode/blob/master/python/0416-partition-equal-subset-sum.py) |Medium|O(m⋅n), m: amount, n: number of elements|O(m)|DP, DFS, memo|*| 1. Convert to subSetSum = sum // 2  2. Similiar as Coin Change DP, but each number can only be used once (thus DP[i] update in a reverse order) | 2020-10-18 |
|464|[Can I Win](https://github.com/teslamyesla/leetcode/blob/master/python/0464-can-i-win.py) |Medium|O(n * 2^n)|O(2^n)|DFS, memo|*| memo[tuple(nums)]; at my turn, if the max(allowed) >= target, then I will win. Otherwise, I choose from the allowed values one by one and recursively call for the other player. If with any choice the opponent fails, then also I can win. | 2020-10-27 |
|473|[Matchsticks to Square](https://github.com/teslamyesla/leetcode/blob/master/python/0473-matchsticks-to-square.py) |Medium|O(4^n)|O(n)|DFS, memo, backtracking|*| for i in range(4): sums[i] += nums[idx]; dfs; sums[i] -= nums[idx] | 2020-10-19 |
|486|[Predict the Winner](https://github.com/teslamyesla/leetcode/blob/master/python/0486-predict-the-winner.py) |Medium|O(n^2)|O(n^2)|DFS, memo|*| memo[(start, end)] tracks absolute max positive delta given (start, end) position regardless of the players picking order! | 2020-10-26 |
|494|[Target Sum](https://github.com/teslamyesla/leetcode/blob/master/python/0494-target-sum.py) |Medium|O(l*n), l: range of sum, n: number of elements|O(l*n)|DFS, memo|*| memo[(target, idx)] = dfs(idx+1, target-nums[idx]) + dfs(idx+1, target+nums[idx]) | 2020-10-22 |
|518|[Coin Change 2](https://github.com/teslamyesla/leetcode/blob/master/python/0518-coin-change-2.py) |Medium|O(S*n), S: amount, n: number of coins|O(n)|DP|*| if i == coin: F[i] += 1; else F[i] += F[i-coin] for coin in coins | 2020-10-21 |
|805|[Split Array With Same Average](https://github.com/teslamyesla/leetcode/blob/master/python/0805-split-array-with-same-average.py) |Hard|O(2^(n/2))|O(2^(n/2))|DP|*| Key trick is sum/n = sum1/k = sum2/(n-k) => only need to enter dfs when satisfying sum * k % n == 0! | 2020-10-24 |
|877|[Stone Game](https://github.com/teslamyesla/leetcode/blob/master/python/0877-stone-game.py) |Medium|O(n^2)|O(n^2)|DP, DFS, memo|*| Almost same as 486 "Predict the Winner" problem, max min dp | 2020-10-29 |
|956|[Tallest Billboard](https://github.com/teslamyesla/leetcode/blob/master/python/0956-tallest-billboard.py) |Hard|O(n*s)|O(n*s)|DP, DFS, memo|*| Really hard problem with a lot of tricks both in DP and DFS solution! see py file for details | 2020-10-25 |
|1049|[Last Stone Weight II](https://github.com/teslamyesla/leetcode/blob/master/python/1049-last-stone-weight-ii.py) |Medium|O(m⋅n), m: sum(stones)//2, n: number of stones|O(m)|DP|*| 1. Key trick is to transform problem to find target cloest to sum(stones) // 2; 2. dp[i] stores max amount achievable that <= i | 2020-10-23 |
|1140|[Stone Game II](https://github.com/teslamyesla/leetcode/blob/master/python/1140-stone-game-ii.py) |Medium|O(n^2)|O(n^2)|DP, DFS, memo|y| max min dp, memo records future sum of Alex starting from idx | 2020-10-30 |
|1406|[Stone Game III](https://github.com/teslamyesla/leetcode/blob/master/python/1406-stone-game-iii.py) |Hard|O(n)|O(n)|DP, DFS, memo|*| max min dp, trick: dfs returns diff instead of absolute value of the first picker | 2020-10-31 |
|1510|[Stone Game IV](https://github.com/teslamyesla/leetcode/blob/master/python/1510-stone-game-iv.py) |Hard|O(n*sqrt(n))|O(n)|DFS, memo|*| for i in range(1,int(math.sqrt(n))+1): if not dfs(n-i*i, memo): return True | 2020-11-01 |

LintCode
========

### LintCode algorithm &hearts;

### Binary Search
| # | Title | Difficulty | Time | Space | Tag | Legend | Note | Last Submission Date |
|---| ----- | ---------- | ---- | ----- | --- | ------ | ---- | -------------------- |
|14|[First Position of Target](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0014-first-position-of-target.py) |Easy|O(logn)|O(1)|Binary Search|y| NA | 2020-10-20 |
|458|[Last Position of Target](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0458-last-position-of-target.py) |Easy|O(logn)|O(1)|Binary Search|y| NA | 2020-10-20 |
|462|[Total Occurrence of Target](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0462-total-occurrence-of-target.py) |Easy|O(logn)|O(1)|Binary Search|y| NA | 2020-10-20 |

### Two Pointers
| # | Title | Difficulty | Time | Space | Tag | Legend | Note | Last Submission Date |
|---| ----- | ---------- | ---- | ----- | --- | ------ | ---- | -------------------- |
|5|[Kth Largest Element](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0005-kth-largest-element.py) |Medium|O(n)|O(1)|Quick Select, Partition, Heap|y| Mirror of Kth Smallest Numbers in Unsorted Array, classic Quick Select problem  | 2020-11-09 |
|31|[Partition Array](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0031-partition-array.py) |Medium|O(n)|O(1)|Partition|y| NA  | 2020-11-09 |
|49|[Sort Letters by Case](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0049-sort-letters-by-case.py) |Medium|O(n)|O(1)|Partition|y| Python string is immutable, solution has a problem there | 2020-11-04 |
|57|[3Sum](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0057-3sum.py) |Medium|O(n^2)|O(1)| Two Pointers |y| 1. Sort numbers 2. Pay attention to two dedup places | 2020-11-09 |
|143|[Sort Colors II](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0143-sort-colors-ii.py) |Medium|O(nlogk), n is len of numbers, k is len of colors|O(1)|Quick Sort|*| Partition [index_from, index_to]，color_pivot=(color_from+color_to)//2, <=color_pivot goes to left，>color_pivot goes to right | 2020-11-06 |
|144|[Interleaving Positive and Negative Numbers](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0144-interleaving-positive-and-negative-numbers.py) |Medium|O(n)|O(1)|Partition, Two Pointers|*| First partition, then two pointers exchange. Pay attention to 3 situations of len_pos, len_neg! | 2020-11-03 |
|148|[Sort Colors](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0148-sort-colors.py) |Medium|O(n)|O(1)|Partition, Two Pointers|*| Classic problem, 3 solutions: 1) counting values 2) two partitions 3) two pointers one pass | 2020-11-04 |
|228|[Middle of Linked List](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0228-middle-of-linked-list.py) |Naive|O(n)|O(1)|Fast Slow Pointers|*| Classic problem, pay attention to return center left of center right (center left: fast=head.next; center right: fast=head) | 2020-11-05 |
|373|[Partition Array by Odd and Even](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0373-partition-array-by-odd-and-even.py) |Easy|O(n)|O(1)|Partition|y| NA | 2020-11-03 |
|461|[Kth Smallest Numbers in Unsorted Array](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0461-kth-smallest-numbers-in-unsorted-array.py) |Medium|O(n)|O(1)|Quick Select, Partition, Heap|*| Classic Quick Select problem | 2020-11-03 |
|464|[Sort Integers II](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0464-sort-integers-ii.py) |Easy|O(nlogn)|O(1)|Quick Sort|*| Classic Quick Sort | 2020-11-06 |
|521|[Remove Duplicate Numbers in Array](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0521-remove-duplicate-numbers-in-array.py) |Easy|O(nlogn)|O(1)|Two Pointers|*| Classic problem, similiar as Move Zeros problem | 2020-11-05 |
|539|[Move Zeroes](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0539-move-zeroes.py) |Easy|O(n)|O(1)|Two Pointers|*| Classic problem, in-place new (left pointer) old (right pointer) array | 2020-11-05 |
|608|[Two Sum II - Input array is sorted](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0608-two-sum-ii-input-array-is-sorted.py) |Medium|O(n)|O(1)|Two Pointers|y| NA | 2020-11-06 |
|894|[Pancake Sorting](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0894-pancake-sorting.py) |Medium|O(n^2)|O(1)|Bubble Sort|*| Idea similiar as bubble sort: put sorted parts to end of array, find max in unsorted part, flip to beginning then flip to len, len-- | 2020-11-04 |


### BFS & Topological Sort
| # | Title | Difficulty | Time | Space | Tag | Legend | Note | Last Submission Date |
|---| ----- | ---------- | ---- | ----- | --- | ------ | ---- | -------------------- |
|7|[Serialize and Deserialize Binary Tree](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0007-serialize-and-deserialize-binary-tree.py) |Medium| O(n)| O(n)|BFS|y| Use BFS for both serialize and deserialize | 2020-12-25 |
|69|[Binary Tree Level Order Traversal](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0069-binary-tree-level-order-traversal.py) |Easy| O(n)| O(n)|BFS|y| pop left of list: queue.pop(0) | 2020-12-18 |
|70|[Binary Tree Level Order Traversal II](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0070-binary-tree-level-order-traversal-ii.py) |Medium| O(n)| O(n)|BFS|y| insert to left of list: nums.insert(0, value) | 2020-12-18 |
|71|[Binary Tree Zigzag Level Order Traversal](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0071-binary-tree-zigzag-level-order-traversal.py) |Medium| O(n)| O(n)|BFS|y| if from_left: level.append(node.val); else: level.insert(0, node.val) | 2020-12-18 |
|120|[Word Ladder](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0120-word-ladder.py) |Hard| O(26*(m^2)×n), m is len of each word, n is # of words| O(m*n)|BFS|*| BFS, get_next_word is the core part: for char in "abcdefghijklmnopqrstuvwxyz": next_words.append(word[:i]+char+word[i+1:]) | 2020-12-25 |
|127|[Topological Sorting](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0127-topological-sorting.py) |Medium| O(V+E)| O(V)|Topology Sort|y| NA | 2020-12-25 |
|137|[Clone Graph](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0137-clone-graph.py) |Medium| O(N+E)| O(N)|BFS in Graph|*| Classic Problem! Recurrsive or Iterative! Push nodes to queue with BFS order, create new node and use visited to track mapping when pushing a node, update neighbors when poping the node to push neighbors | 2020-12-24 |
|178|[Graph Valid Tree](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0178-graph-valid-tree.py) |Medium| O(n)| O(n)|DFS / Union Find|*| 3 properties of tree: 1) connectivity 2) n-1 edges for n node tree 3) no cycle. Satisfy any 2 of above qualifies for a tree. DFS checks 1+2, Union Find checks 2+3 | 2020-10-14 |
|242|[Convert Binary Tree to Linked Lists by Depth](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0242-convert-binary-tree-to-linked-lists-by-depth.py) |Easy| O(n)| O(n)|BFS|y| BFS level order traversal | 2020-12-21 |
|431|[Connected Component in Undirected Graph](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0431-connected-component-in-undirected-graph.py) |Medium| O(V+E) | O(V) | DFS / Union Find|*| NA | 2020-10-14 |
|433|[Number of Islands](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0433-number-of-islands.py) |Easy| O(m*n)| O(min(m,n))|BFS/DFS in Graph|*| For each place in grid: if equals 1, count + 1, do BFS/DFS | 2020-12-21 |
|573|[Build Post Office II](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0573-build-post-office-ii.py) |Hard| O(H*m*n), H is # of houses| O(m*n)| BFS in Graph|*| Try every empty place will TLE! Instead, BFS from every house, when reaching every empty place, update how many houses it has been touched and sum of dist from touched houses | 2020-12-23 |
|598|[Zombie in Matrix](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0598-zombie-in-matrix.py) |Medium| O(m*n)| O(m*n)|Multi-Source BFS in Graph|*| Similiar as topology sort, queue all sources and propogate. 1) no need to keep visited tracker, can tell visited by value 2) days is # of levels, days - 1 is # of propogations | 2020-12-23 |
|605|[Sequence Reconstruction](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0605-sequence-reconstruction.py) |Medium| O(N+E)| O(N+E)|Topology Sort|*| Topology Sort with differences in format of neighbors and uniqueness of topology order | 2020-12-24 |
|611|[Knight Shortest Path](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0611-knight-shortest-path.py) |Medium| O(m*n)| O(m*n)|BFS in Graph|*| Always mark visited before pushing to queue! Instead of after poping from queue (because for the ones already in queue but haven't been poped yet, we don't want to push the nodes to queue again)!  | 2020-12-24 |
|615|[Course Schedule](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0615-course-schedule.py) |Medium| O(N+E)| O(N+E)|Topology Sort|y| Topology Sort | 2020-12-23 |
|616|[Course Schedule II](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0616-course-schedule-ii.py) |Medium| O(N+E)| O(N+E)|Topology Sort|y| Topology Sort | 2020-12-23 |
|618|[Search Graph Nodes](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0618-search-graph-nodes.py) |Medium| O(N+E)| O(N)|BFS in Graph|y| BFS in Graph, keep visited tracker | 2020-11-11 |
|892|[Alien Dictionary](https://github.com/teslamyesla/leetcode/blob/master/python/lintcode-0892-alien-dictionary.py) |Hard| O(V+E)=O(n*k), n: # of words, k: avg word length| O(V+E)=O(n*k)|Topology Sort|*| 1. char is the node, char to char relationship is the dependency, use topology sort 2. use HEAP instead of Queue to maintain lexicographical order during topological sort! | 2020-12-21 |

### Reference
残酷刷题群 youtube: https://docs.google.com/spreadsheets/d/1kBGyRsSdbGDu7DzjQcC-UkZjZERdrP8-_QyVGXHSrB8/htmlview?urp=gmail_link&gxids=7757#
基础算法(三) -- DFS: https://docs.google.com/presentation/d/1pU6V3tGvldbAXk_qrcNOqE85vfv9Ty-raBP2XcDacyo/edit#slide=id.p
