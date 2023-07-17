from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []

        node = head
        while node:
            vals.append(node.val)
            node = node.next
        
        hasGreater = [False] * len(vals)
        stk = []
        for i in range(len(vals)):
            while stk and vals[stk[-1]] < vals[i]:
                hasGreater[stk.pop()] = True
            stk.append(i)

        node = prev = head
        i = 0
        while node:
            if hasGreater[i]:
                if node == head:
                    head = head.next
                    prev = head
                else:
                    while node and hasGreater[i]:
                        node=node.next
                        i += 1
                    prev.next = node

            prev = node
            node = node.next
            i += 1

        return head
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stk = []

        node = head
        while node:
            while stk and stk[-1].val < node.val:
                stk.pop()
            stk.append(node)
            node = node.next
        
        for i in range(len(stk)-1):
            stk[i].next = stk[i+1]

        return stk[0]