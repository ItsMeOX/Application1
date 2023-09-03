from typing import Optional

# Maybe keep tracking of 'prev' is better than node.next

# Set a dummy list node before head node, because we might want to insert before head node.
# Then we keep track of current node using 'node', and prev node using 'prev'.
# Then traverse through the linked list,
# if val of current node < val of prev node,
# then we set 'cursor' which iterate through the linked list from dummy and stop when val of next node is larger than value of current node.
# Then we insert 'node' at position 'cursor'.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        node = prev = head
        while node:
            if node.val < prev.val:
                prev.next = node.next
                cursor = dummy
                while cursor.next.val < node.val:
                    cursor = cursor.next
                temp = cursor.next
                cursor.next = node
                node.next = temp
                node = prev.next
            else:
                prev = node
                node = node.next
        
        return dummy.next