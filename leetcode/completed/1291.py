from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nums = '123456789'
        res = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                num = int(nums[i:j+1])
                if low <= num:
                    if num <= high:
                        res.append(num)
                    else:
                        break
        res.sort()
        return res
        


sol = Solution()
print(sol.sequentialDigits(100, 300))
        