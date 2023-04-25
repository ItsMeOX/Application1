# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return
        
        cur = head
        count = 0
        while cur:
            cur = cur.next
            count += 1


        cur = dummy = head


        for _ in range(count - n - 1):
            cur = cur.next

        if n == count:
            return dummy.next
        elif cur.next:
            cur.next = cur.next.next
        else:
            cur.next = None

        

        return dummy
        
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         slow = head
#         fast = head

#         for _ in range(n):
#             fast = fast.next
        
#         if not fast:
#             return head.next
        
#         while fast.next:
#             slow = slow.next
#             fast = fast.next
        
#         slow.next = slow.next.next

#         return head