from typing import Optional

# Perform DFS to child first, then to the next node.
# If current node has child, set node <-> node.child
# Get the last node of node.child and set last_child_node <-> node.next
# Here we return the last node by using next_node or node (if next_node is null then return this node).
# Note that node.next might be null, so remember to take care of that.

# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        def dfs(node):
            if not node: return None

            if node.child:
                last_child_node = dfs(node.child)
                last_child_node.next = node.next
                if node.next:
                    node.next.prev = last_child_node
                node.next = node.child
                node.child.prev = node
                node.child = None
            
            next_node = dfs(node.next)
            return next_node or node

        dfs(head)

        return head
    
# Because we will bring up the child node to next node,
# we will eventually reach child node of child node which which has child also.

#cur
# A - B - C
#     |
#     D - E
#     |
#     F - G

#    cur
# A - B - D - E - C
#         |
#         F - G

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        node = head
        while node:
            if node.child:
                last_child_node = node.child
                
                while last_child_node.next:
                    last_child_node = last_child_node.next

                last_child_node.next = node.next
                if node.next:
                    node.next.prev = last_child_node
                node.next = node.child
                node.child.prev = node
                node.child = None

            node = node.next
        
        return head