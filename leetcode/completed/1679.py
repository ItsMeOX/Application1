from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        memo = {}
        res = 0

        for num in nums:
            memo[num] = memo.get(num, 0) + 1

        for num in nums:
            if memo[num] > 0:
                memo[num] -= 1
                if k - num in memo and memo[k - num] > 0:
                    memo[k - num] -= 1
                    res += 1
        return res

        # [/,/,/,/,/,/,/,/,/,4,4,/,2,/,2,2,3,2,4,2]
        # {2: 5, 5: 0, 4: 3, 1: 0, 3: 1}
        # res: 1
