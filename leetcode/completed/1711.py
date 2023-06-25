from typing import List
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        count = {}
        res = 0
        MOD = 10 ** 9 + 7

        for d in deliciousness:
            temp = 1
            for _ in range(22):
                if temp - d in count:
                    res += count[temp-d]
                temp <<= 1
            count[d] = count.get(d, 0) + 1
                
        return res % MOD
    
sol = Solution()
print(sol.countPairs([1,1,1,3,3,3,7,2,2,1,3,5]))