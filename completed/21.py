# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

#         if head == None:
#             return head
        
#         self.res = ListNode(head.val, None)
#         node = head.next
        
#         if node == None:
#             return head

#         while node.next != None:
#             self.res = ListNode(node.val , self.res)
#             node = node.next
#         else:
#             self.res = ListNode(node.val , self.res)
#             return self.res
        
f


class Solution:
    def reverseList(self, head: Optional[ListNoteBook]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            
            

        return prev

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.res = None

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #print(head, self.res)
        if head == None:
            print(self.res)
            return self.res

        self.res = ListNode(head.val , self.res) 

        self.reverseList(head.next)
        
        