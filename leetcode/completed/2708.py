from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        pos = []
        neg = []

        for num in nums:
            if num > 0: pos.append(num)
            if num < 0: neg.append(num)
        
        if len(neg) & 1:
            neg.remove(max(neg))
        
        if len(pos) == len(neg) == 0:
            return 0

        res = 1
        for x in pos: res *= x
        for x in neg: res *= x
        return res


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # if 0 and 1 negative num in nums: return 0
        # if cnt of 0 == len(nums)       : return 0
        def checkException():
            cnt_neg = 0
            cnt_zero = 0
            for num in nums:
                if num > 0: return
                if num == 0: cnt_zero += 1
                if num < 0: cnt_neg += 1
            if cnt_zero != 0 and cnt_neg == 1:
                return True
            if cnt_zero == len(nums):
                return True
            
        if checkException(): return 0
        
        max_neg = -float('inf')
        res = 1

        for num in nums:
            if num != 0:
                if num < 0:
                    max_neg = max(max_neg, num)
                res *= num
        
        if res < 0:
            res //= max_neg
                
        
        return res