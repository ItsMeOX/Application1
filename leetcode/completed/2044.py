from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_OR = 0
        res = 0
        for num in nums:
            max_OR |= num

        def dfs(i, current):
            nonlocal res
            if i == len(nums): return 

            dfs(i+1, current)
            current |= nums[i]
            if current == max_OR: res += 1
            dfs(i+1, current)

        dfs(0, 0)

        return res
    

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        counter = {0: 1}
        for num in nums:
            for key, value in list(counter.items()):
                counter[key | num] = counter.get(key | num, 0) + value
            
        return counter[max(counter)]