from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = dummy = ListNode()
        carry = 0
        while l1 or l2:
            if l1 and l2:
                new_val = l1.val + l2.val
            elif l1:
                new_val = l1.val
            else:
                new_val = l2.val

            if carry:
                new_val += carry
                carry -= 1

            # this also works
            # if carry:
            #     if new_val == 9:
            #         new_val = 0
            #     else:
            #         new_val += carry
            #         carry -= 1

            if new_val > 9:
                new_val -= 10
                carry += 1
                
            dummy.next = ListNode(new_val)
            dummy = dummy.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            dummy.next = ListNode(carry)

        return res.next