"""
Time: O(h + k), h is the height of tree, k is the input parameter
Space: O(h)

Reference: https://www.jiuzhang.com/problem/closest-binary-search-tree-value-ii/

建议大家还是掌握这个时间复杂度O(k+logn)的解法, 要不然面试的评级肯定不会高，即使做出来O(n) 又有什么用呢, 毕竟题目中出现k就是希望你能用它来减少时间复杂度的
方法如下: 首先建立两个数组prev和next用来储存比target小的node和比它大的node, 再用while k去遍历k个数，提前取出他们的值，比较大小，再调用方法getNext或getPrev即可
实现get_next()，利用next_stack寻找next_value。 在一般的BST iterator中，寻找下一节点的算法是：如果当前点存在右子树，那么就是右子树中一直向左走到底的那个点；如果当前点不存在右子树，则对到达当前点的路径进行反向遍历（一直pop stack），寻找第一个（离当前点最近的）左拐的点。 然而在本题中，因为已经分离prev_stack和next_stack，所以在当前节点不存在右子树的情况下，当前节点在next_stack中的前一个位置自然就是要找的下一个点。因此代码中只需处理当前节点存在右子树时的情况，即先取当前节点的右子树，再一路向左走到底。
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
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # write your code here
        prev, next = [], []
        
        while root:
            if root.val < target:
                prev.append(root)
                root = root.right
            elif root.val > target:
                next.append(root)
                root = root.left
            else:
                next.append(root)
                break
        
        res = []    
        while k:
            prev_diff = float('inf') if not prev else abs(prev[-1].val - target)
            next_diff = float('inf') if not next else abs(next[-1].val - target)
            
            if not prev and not next:
                break
            elif prev_diff < next_diff:
                res.append(prev[-1].val)
                self.getPrev(prev)
            else:
                res.append(next[-1].val)
                self.getNext(next)
            k -= 1
            
        return res
        
    def getPrev(self, prev):
        node = prev.pop()
        node = node.left
        while node:
            prev.append(node)
            node = node.right
        
    def getNext(self, next):
        node = next.pop()
        node = node.right
        while node:
            next.append(node)
            node = node.left
        
            
            
