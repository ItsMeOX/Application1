from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        if head.val >= x:
            last_node = head
            while last_node.next:
                if last_node.next.val < x:
                    temp = last_node.next.next
                    temp_head = head
                    head = last_node.next
                    last_node.next.next = temp_head
                    last_node.next = temp
                    break
                else:
                    last_node = last_node.next

        last_node = head # last node which val is >= x
        while last_node.next and last_node.next.val < x:
            last_node = last_node.next

        node = last_node
        while node.next:
            if node.next.val < x:
                temp = node.next.next
                node.next.next = last_node.next
                last_node.next = node.next
                node.next = temp
                last_node = last_node.next
            else:
                node = node.next
        
        return head
        

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        greater_head = greater_tail = ListNode(0)
        lesser_head  = lesser_tail  = ListNode(0)

        while head:
            if head.val < x:
                lesser_tail.next = head
                lesser_tail = lesser_tail.next
            else:
                greater_tail.next = head
                greater_tail = greater_tail.next
            head = head.next
        
        greater_tail.next = None
        lesser_tail.next = greater_head.next

        return lesser_head.next
                
                    
