"""
Time: O(n)
Space: O(1)
"""

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    """
    Note: 注意fast初始化是head.next，为了让fast多走一小步，来确保even时return center left one
    比如1->2->3->4，return center left one是2，那么slow只能走一次，如果fast initialize成head, 要走两次，slow就会指向3而不是2了
    
    如果return center right one，那么fast初始化成head, same as slow
    """
    
    def middleNode(self, head):
        # write your code here
        if head is None or head.next is None:
            return head
            
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
        
        
        
