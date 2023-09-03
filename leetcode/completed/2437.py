class Solution:
    def countTime(self, time: str) -> int:
        res = 0

        h1, h2 = time[0], time[1]
        m1, m2 = time[3], time[4]

        res = 1

        if h1 == h2 == '?':
            res *= 24
        elif h1 == '?':
            if int(h2) < 4:
                res *= 3
            else:
                res *= 2
        elif h2 == '?':
            if int(h1) == 2:
                res *= 4
            else:
                res *= 10
        
        if m1 == m2 == '?':
            res *= 60
        elif m1 == '?':
            res *= 6
        elif m2 == '?':
            res *= 10
        
        return res
    