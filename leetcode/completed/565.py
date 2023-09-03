from typing import List

# Here because that all the values in nums are UNIQUE, so it is impossible to form cycle with tails,
# the cycle formed can only be perfect cycle.

# O(n), O(n)
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        def dfs(i):
            if i in visited:
                return 0
            visited.add(i)
            return 1 + dfs(nums[i])

        res = 0
        visited = set()
        for i in range(len(nums)):
            res = max(res, dfs(i))
        
        return res
    
# Keep track of visited number by using a set 'visited'.
# Loop i from 0 to len(nums)-1, if we have not visited i, add 1 to cur_len and traverse to nums[i] until we traverse to i that we have visited before.
# Compare and update 'res' with 'cur_len' each iteration.

# O(n), O(n)
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:

        res = 0
        visited = set()
        for i in range(len(nums)):
            cur_len = 0
            while i not in visited:
                visited.add(i)
                i = nums[i]
                cur_len += 1

            res = max(res, cur_len)
        
        return res
    
# O(n), O(1), but modified input.
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            cur_len = 0
            while nums[i] != -1:
                nums[i], i = -1, nums[i]
                cur_len += 1

            res = max(res, cur_len)
        
        return res