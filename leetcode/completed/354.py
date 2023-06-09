class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int: # tried with O(n^2) method, got TLE
        envelopes.sort(key = lambda e: (e[0], -e[1]))
        dp = [envelopes[0][1]]

        def search(target):
            l , r = 0 , len(dp) - 1
            while l != r:
                m = (l+r) // 2
                if dp[m] > target:
                    r = m
                elif dp[m] < target:
                    l = m + 1
                else:
                    return m
            return l

        for e in envelopes:
            if e[1] > dp[-1]:
                dp.append(e[1])
            else:
                dp[search(e[1])] = e[1]

        return len(dp)