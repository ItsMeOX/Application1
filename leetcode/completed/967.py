from typing import List

# If last digit of current number (current number % 10) -k >= 0
# or
# if last digit of current number (current number % 10) +k <= 9
# then append this digit to last digit of current number by shifting number left once and adding this digit.
# We start backtracking at every digit from 1 to 9.

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def backtrack(s):
            if len(str(s)) == n:
                res.append(s)
                return

            if s%10 - k >= 0:
                backtrack(s * 10 + s % 10 - k)
            
            if k and s%10 + k <= 9: # 'if k' because if k == 0 we do not want duplicate value.
                backtrack(s * 10 + s % 10 + k)
        
        res = []
        for i in range(1, 10):
            backtrack(i)
        return res

sol = Solution()
print(sol.numsSameConsecDiff(n = 2, k = 1))
print([10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98])