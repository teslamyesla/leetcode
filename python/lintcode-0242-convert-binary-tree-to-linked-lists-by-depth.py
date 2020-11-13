"""
Time: O(n)
Space: O(n)
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        if root is None:
            return []
            
        queue = [root]
        res = []
        
        while queue:
            level_dummy = ListNode(0)
            level_curr = level_dummy
            for _ in range(len(queue)):
                node = queue.pop(0)
                level_curr.next = ListNode(node.val)
                level_curr = level_curr.next
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_curr.next = None
            res.append(level_dummy.next)
            
        return res
                
