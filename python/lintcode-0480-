"""
Time complexity: O(n)
Space complexity: O(n) / output can be O(n^2)

Reference: https://www.lintcode.com/problem/binary-tree-paths/solution
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    
    """
    Solution 2: Divide and Conquer
    """
    def binaryTreePaths(self, root):
        if root is None:
            return []
        
        # 99% 的题，不用单独处理叶子节点
        # 这里需要单独处理的原因是 root 是 None 的结果，没有办法用于构造 root 是叶子的结果    
        if root.left is None and root.right is None: # root is leaf
            return [str(root.val)]
            
        left_paths = self.binaryTreePaths(root.left)
        right_paths = self.binaryTreePaths(root.right)
        
        res = []
        for path in left_paths + right_paths:
            res.append(str(root.val) + '->' + path)
        
        return res
    
    """
    Solution 1: Traversal DFS
    
    def binaryTreePaths(self, root):
        # write your code here
        if root is None:
            return []
            
        res = []
        self.dfs(root, [str(root.val)], res) # path already include current node
        return res
        
    def dfs(self, node, path, res):
        if node is None:
            return res
            
        if node.left is None and node.right is None: # node is leaf
            res.append('->'.join(path)) # path already include current node
            return res
            
        if node.left:
            path.append(str(node.left.val))
            self.dfs(node.left, path, res)
            path.pop() # 回溯
            
        if node.right:
            path.append(str(node.right.val))
            self.dfs(node.right, path, res)
            path.pop() # 回溯
    """
