"""
Time: O(n)
Space: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Reference: https://www.lintcode.com/problem/intersection-of-two-linked-lists/solution
思路：后半段是一样的，因此先算长度，把head挪到长度一样的节点后，再开始逐个节点比较，直到抵达共同节点
"""

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)
        
        while lenA > lenB:
            headA = headA.next
            lenA -= 1
            
        while lenB > lenA:
            headB = headB.next
            lenB -= 1
            
        # reach same length
        while headA:
            if headA == headB:
                return headA
            headA, headB = headA.next, headB.next
            
        return None
        
    def getLength(self, head):
        if head is None:
            return 0
        
        length = 0
        curr = head
        
        while curr:
            length += 1
            curr = curr.next
            
        return length
        
