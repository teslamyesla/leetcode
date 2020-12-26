"""
Time: O(N)
Space: O(N)
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
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        if root is None:
            return ""
            
        res = []
        queue = [root]
        
        while queue:
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node is None:
                    res.append('#')
                else:
                    res.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                
        return ",".join([str(x) for x in res])

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here
        if data == "":
            return None
            
        res = data.split(",")
        root = TreeNode(int(res[0]))
        queue = [root]
        
        idx = 1
        while queue:
            node = queue.pop(0)
            left, right = res[idx], res[idx + 1]
            if left != '#':
                node.left = TreeNode(int(left))
                queue.append(node.left)
            if right != '#':
                node.right = TreeNode(int(right))
                queue.append(node.right)
            idx += 2
            
        return root
        
        
        
        
        
        
