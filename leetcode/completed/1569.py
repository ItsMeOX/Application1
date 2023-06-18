from math import comb
class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10 ** 9 + 7

        def dfs(tree):
            if len(tree) < 3:
                return 1

            left_subtree = [n for n in tree if n < tree[0]]
            right_subtree = [n for n in tree if n > tree[0]]
            return comb(len(tree)-1, len(left_subtree)) * dfs(left_subtree) * dfs(right_subtree)

        return (dfs(nums)-1) % MOD
    
# observation: 
# example arr: [3,4,5,1,2]
# if root = 3, left_subtree will be [1,2], right_subtree will be [4,5]
# as long as the relative position of left and right subtree does not change, the BST tree will not change its structure

# [1,2,4,5]
# [1,4,2,5]
# [1,4,5,2]
# [4,5,1,2]
# [4,1,2,5]
# [4,1,5,2]

# the number of ways to fit left and right subtree into an array of length len(left_subtree) + len(right_subtree) is
# ( len(tree)-1 ) C ( len(left_subtree) or len(right_subtree) )

# and the same goes for left and right sub trees
