from typing import List

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for _ in range(len(nums)//k):
            _min = min(count.keys())

            for i in range(_min, _min+k):
                if _min + i not in count:
                    return False
                count[_min+i] -= 1
                if count[_min+i] == 0:
                    del count[_min+i]

        return True

    
sol = Solution()
print(sol.isPossibleDivide(nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3))