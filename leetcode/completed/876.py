# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        count = 0
        while current:
            current = current.next
            count += 1
        current = head
        for _ in range(count//2):
            current = current.next
        return current
