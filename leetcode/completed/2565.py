from typing import List

# nums = [1,2,3,4,5], k = 3

#   ( 1 + 2 + ... + m+k-1 ) - ( 1 + 2 + ... + m-1 )
# = (1+2+3+4+5+6+7) - (1+2+3+4)
# = 5+6+7
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        m = max(nums)
        return (m+k-1)*(m+k) // 2 - (m-1)*(m) // 2

#   (m * k) + ( 1 + 2 + ... + k-1 )
# = (5 * 3) + ( 1 + 2 )
# = 5+6+7
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return max(nums)*k + (k-1)*k//2