from typing import Optional

# My approach:
# Convert singly-linked list into doubly-linked list,
# Starting from value of last node in linked list, list[i] *= 2,
# if list[i] > 9, carry += 1, list[i] %= 10.
# If there is carry, then list[i] += 1.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        node = head
        while node.next:
            node.prev = prev
            prev = node
            node = node.next
        node.prev = prev

        carry = 0
        while node:
            carry_temp = 0
            node.val *= 2
            if node.val > 9:
                carry_temp = 1
                node.val %= 10
            if carry and node.val < 9:
                carry -= 1
                node.val += 1
            carry += carry_temp
            if not node.prev:
                node.prev = ListNode(carry)
                node.prev.next = node
                node = node.prev
                break
            node = node.prev

        if node.val == 0: return node.next
        return node

# We first double the value of current node by 2 and % 10 first.    
# Notice that if next digit > 4, then there will be a carry of 1.
# so if next digit > 4, add 1 to current node.

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val > 4:
            head = ListNode(0, head)
        
        node = head
        while node:
            node.val = (node.val*2) % 10
            if node.next and node.next.val > 4:
                node.val += 1
            node = node.next
        
        return head