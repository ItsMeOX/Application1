class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        counter = {}
        res = 0

        for i in range(len(s)):
            counter[s[i]] = counter.get(s[i], 0) + 1            

            if i > 1:
                for val in counter.values():
                    if val > 1: break
                else:
                    res += 1
                counter[s[i-2]] -= 1

        return res
    
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res = 0

        for i in range(2, len(s)):
            if s[i-2] != s[i-1] and s[i-1] != s[i] and s[i-2] != s[i]:
                res += 1

        return res