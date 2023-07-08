from typing import List

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0:
            return True

        memo = {}

        def minimax(left, right):
            if left == right:
                return nums[left]

            if (left, right) in memo:
                return memo[(left, right)]

            l = nums[left] - minimax(left+1, right)
            r = nums[right] - minimax(left, right-1)

            memo[(left, right)] = max(l, r)

            return memo[(left, right)]
        
        return minimax(0, len(nums)-1) >= 0