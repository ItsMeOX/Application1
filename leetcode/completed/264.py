class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        x2p , x3p , x5p = 0 , 0 , 0
        while len(res) < n:
            x2 = 2 * res[x2p]
            x3 = 3 * res[x3p]
            x5 = 5 * res[x5p]

            x = min(x2,x3,x5)

            if x2 == x:
                x2p += 1
            elif x3 == x:
                x3p += 1
            else:
                x5p += 1
            if x != res[-1]:
                res.append(x)

        return res[-1]
        




    

sol = Solution()
print(sol.nthUglyNumber(100000))