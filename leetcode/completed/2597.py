from typing import List

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        res = 0
        current = {}

        def dfs(i):
            nonlocal res
            if i == len(nums): return

            current[nums[i]] = current.get(nums[i], 0) + 1
            if nums[i]-k not in current and k+nums[i] not in current:
                res += 1
                dfs(i+1)
            current[nums[i]] -= 1
            if current[nums[i]] == 0:
                del current[nums[i]]
            dfs(i+1)

        dfs(0)
        return res