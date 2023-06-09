class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while (a | b != c):
            if (c & 1):
                if not (a & 1 or b & 1):
                    flips += 1 
            else:
                if (a & 1 and b & 1):
                    flips += 2
                elif (a & 1 or b & 1):
                    flips += 1
            a >>= 1
            b >>= 1
            c >>= 1
        
        return flips

sol = Solution()
print(sol.minFlips(a = 8, b = 3, c = 5))
# 1000 8   0010 2
# 0011 3   0110 6
# -------------------
# 0101 5   0101 5