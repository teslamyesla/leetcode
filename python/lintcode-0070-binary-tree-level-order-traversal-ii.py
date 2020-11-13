"""
Time: O(n)
Space: O(n)

Notes:
1. node = queue.pop(0)
2. res.insert(0, level)

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
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrderBottom(self, root):
        # write your code here
        if root is None:
            return []
            
        queue = [root]
        res = []
        
        while queue:
            level = []
            
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            res.insert(0, level)
        
        return res
