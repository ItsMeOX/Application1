from typing import Optional, List

# Create a res array with dummy nodes as head of each res[i].
# Get the length of the linked list and get how many nodes we should put in a list and also the remainder.
# Iterate through the linked list again and put the nodes into res[i] in group 
# (how many should be grouped into one groups + remainder > 0 or not).
# Remember to move dummy node to next nodes for each res[i].

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = [ListNode() for _ in range(k)]

        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        each_count = length // k
        remainder = length - each_count*k

        node = head
        for i in range(k):
            cur_needed = each_count + (remainder > 0)
            node_i = res[i]

            while node and cur_needed > 0:
                node_i.next = node
                node_i = node_i.next
                temp = node.next
                node.next = None
                node = temp
                cur_needed -= 1

            remainder -= 1

        for i in range(len(res)):
            res[i] = res[i].next

        return res