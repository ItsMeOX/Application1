class Solution:
    def minimumSum(self, num: int) -> int:
        s = []
        for _ in range(4):
            s.append(num % 10)
            num //= 10
        s.sort()        

        return s[0]*10 + s[2] + s[1]*10 + s[3]
    
class Solution:
    def minimumSum(self, num: int) -> int:
        s = sorted(str(num))
        return int(s[0] + s[2]) + int(s[1]+s[3])

sol = Solution()
print(sol.minimumSum(2932))