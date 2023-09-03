from functools import lru_cache

# We iterate i from left to right-1 and let i be the root node of each iteration.
# We then determine how many ways are there to build left and right subtrees by iterate i from left to right-1 again 
# until left == right, 
# which means there is one node left,
# then we will return 1.


class Solution:
    def numTrees(self, n: int) -> int:

        @lru_cache(None)
        def dfs(left, right):
            if left == right:
                return 1
            
            res = 0
            for i in range(left, right):
                l = dfs(left, i)
                r = dfs(i+1, right)
                res += l * r

            return res

        return dfs(0, n)