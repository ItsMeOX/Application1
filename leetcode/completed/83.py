from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        cur_node = head
        while cur_node:
            next_node = cur_node.next
            while (next_node and cur_node.val == next_node.val):
                next_node = next_node.next
            cur_node.next = next_node
            cur_node = cur_node.next

        return head