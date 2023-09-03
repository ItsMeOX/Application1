from typing import Optional

# Count the number of nodes in linked list and travel again to the half-1 of linked list 
# then remove the middle node of linked list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        node = head
        while node:
            count += 1
            node = node.next
        
        if count // 2 == 0: return None

        node = head
        for _ in range(count // 2 - 1):
            node = node.next
        node.next = node.next.next

        return head
    
# Use two pointers, fast and slow.
# The fast pointer starts and head.next.next and moves two units each iteration.
# By the end the fast pointer reaches end of list or out of list, 
# the slow pointer will be at 1 node before the middle node,
# and we can just remove the next node of slow pointer.

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        
        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = slow.next.next

        return head