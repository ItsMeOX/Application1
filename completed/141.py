# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        while current:
            if current.next:
                current = current.next.next
                head = head.next
            # else:
            #     return False
            if current == head:
                return True
        return False
    
# slow = head
# while(slow):
# 	if slow.val == None:
# 		# This was already visited
# 		return True
# 	slow.val = None # a way to mark visited
# 	slow = slow.next
# return False