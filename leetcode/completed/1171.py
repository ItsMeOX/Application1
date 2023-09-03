from typing import Optional

# Iterate through list for two times.
# For the first time, 
# we will mark cumulative sum till node i at a hashmap 'seen'.
# for example: 
# 1 2 3 -3 4
# 1 3 6  3 4
# here because 3+(-3) = 0, we will definitely override one existing seen key.
# For the second time,
# calculate cumulative sum till node i again,
# and set the next of current to seen[sums].next .
# for example:
# 1 -> 2 -> 3 -> -3 -> 4
# becomes
# 1 -> 2 -> 4

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        seen = {0: dummy}
        
        sums = 0
        node = head
        while node:
            sums += node.val
            seen[sums] = node
            node = node.next
        
        node = dummy
        sums = 0
        while node:
            sums += node.val
            node.next = seen[sums].next
            node = node.next
        
        return dummy.next

# Worse O(n^2)
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        
        node = head
        while node:
            arr.append(node.val)
            node = node.next
        
        for i in range(len(arr)-1, -1, -1):
            sums = 0
            for j in range(i, len(arr)):
                sums += arr[j]
                if sums == 0:
                    arr = arr[:i] + arr[j+1:]
                    break

        res = dummy = ListNode()

        for val in arr:
            dummy.next = ListNode(val)
            dummy = dummy.next
        
        return res.next