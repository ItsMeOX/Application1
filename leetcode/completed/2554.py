from typing import List

# We convert banned list to banned set so we can get banned number in O(1) time instead of O(n) time.
# Iterate i from 1 to n, greedily adding i to 'cur_sum' until 'cur_sum' exceeds maxSum or i reaches n.
# In the process, we add 1 to 'res' everytime the number is valid and the res eventually will be our answer.

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        res = 0
        cur_sum = 0
        banned = set(banned)
        
        for i in range(1, n+1):
            if i in banned:
                continue
            cur_sum += i
            if cur_sum > maxSum:
                break
            res += 1
    
        return res