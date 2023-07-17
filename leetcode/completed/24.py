from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node and node.next:
            temp = node.next.next
            node.next.next = node
            node.next = temp
            node = temp

        return head
            
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        prev, cur = dummy, head

        while cur and cur.next:
            prev.next = cur.next
            cur.next = cur.next.next
            prev.next.next = cur
            prev = cur
            cur = cur.next
            
        return dummy.next
            


sol = Solution()
print(sol.swapPairs(ListNode(val= 1, next= ListNode(val= 2, next= ListNode(val= 3, next= ListNode(val= 4, next= None))))))