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
经典题目：
当判断有环时(slow==fast)，从头移动慢指针，同时从相遇点移动快指针，两指针再次相遇处即为环的入口

Reference:
1. http://fisherlei.blogspot.com/2013/11/leetcode-linked-list-cycle-ii-solution.html
2. https://www.lintcode.com/problem/linked-list-cycle-ii/solution
3. https://www.jiuzhang.com/problem/linked-list-cycle-ii/#tag-lang-java

证明：环外长度为a, 环长为l, 第一次相遇为b, 快指针走了a + ml + b, 慢指针走了a + nl + b
同时，a + ml + b = 2(a + nl + b) => a + b = (m - n)l，即从b处再走a步就到达环入口

顺口溜：一快一慢一起走，两个碰头慢回头，一步走，一步走。再相遇，就是goal！

Note: 此处第一圈快慢指针相遇判断有环否的写法与lined list cycle I不同，不能直接用I的写法，主要有两点：
1. slow, fast = head, head，都从head出发，而不能slow, fast = head, head.next， 因为要精确保证fast = 2 * slow
2. while判断条件要相应换成: while fast and fast.next，因为初始条件就是slow == fast，不再能使用while slow != fast作为while条件，而把slow是否等于fast的判断放到循环内部
"""

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = self.hasCycle(head)
        if fast is None:
            return None
            
        slow = head
        while slow != fast:
            slow, fast = slow.next, fast.next
            
        return slow
        
    def hasCycle(self, head):
        # if no cycle, return None; else, return the node where slow and fast meet
        if head is None or head.next is None:
            return None
            
        slow = fast = head
        
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return slow
                
        return None
