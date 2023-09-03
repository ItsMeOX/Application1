from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Perform a inorder traversal on root and append the stringified valued if the node exists else 'N' to array 'nodes', which means the node is a leaf node.
# Convert the 'nodes' array to string by using a seperator.

# Deserialize the string passed by splitting the passed in 'data' string with the separator we used.
# Perform another inorder traversal and build the tree again.
# We do this by increasing 'i', which is the index for splitted 'data' array.
# If we encounter 'N' just return None.
# Else, we add a node which has the value of nodes[i].


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        nodes = []
            
        def dfs(node):
            if not node:
                nodes.append('N')
                return

            nodes.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ' '.join(nodes)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        nodes = data.split(' ')
        i = 0

        def dfs():
            nonlocal i
            if nodes[i]  == 'N':
                i += 1
                return None

            node = TreeNode(val = int(nodes[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans