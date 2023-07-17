from typing import List
class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        num = list(num)
        mutated = False
        
        for i, d in enumerate(num):
            cur_d = int(d)
            if change[cur_d] > cur_d:
                num[i] = str(change[cur_d])
                mutated = True
            elif change[cur_d] < cur_d and mutated:
                break

        return "".join(num)
    
sol = Solution()