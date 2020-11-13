"""
Time: O(n)
Space: O(n)

Notes:
1. node = queue.pop(0)
2. from_left = 1 - from_left 
3. if from_left: level.append(node.val); else: level.insert(0, node.val)

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
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        if root is None:
            return []
            
        queue = [root]
        res = []
        from_left = 1
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if from_left:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
            from_left = 1 - from_left
            
        return res
                    
            
            
