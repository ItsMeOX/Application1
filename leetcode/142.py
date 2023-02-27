# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head , head

        while(fast):
            if fast.next:
                fast = fast.next.next
                slow = slow.next
            else:
                return None
            
            if slow == fast:
                fast = head
                while(fast != slow):
                    fast = fast.next
                    slow = slow.next
                return fast
                    



        return None