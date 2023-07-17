class Solution:
    def beautySum(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            cnt = {}
            for j in range(i, len(s)):
                cnt[s[j]] = cnt.get(s[j], 0) + 1
                res += max(cnt.values()) - min(cnt.values())
                
        return res
    
class Solution:
    def beautySum(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            cnt = {}
            for j in range(i, len(s)):
                cnt[s[j]] = cnt.get(s[j], 0) + 1
                res += max(cnt.values()) - min(cnt.values())
                
        return res