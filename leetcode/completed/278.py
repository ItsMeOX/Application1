# The isBadVersion API is already defined for you.

lis = [False,False,True,True,True]

def isBadVersion(version: int) -> bool:
    return lis[int(version)]


class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0
        ans = -1

        while low <= n:
            middle = (low + n) // 2
            if isBadVersion(middle):
                ans = middle
                n = middle - 1
            else:
                low = middle + 1

        return ans
            
                
sol = Solution()
print(sol.firstBadVersion(3))



