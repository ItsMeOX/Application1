class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        current_idx = 0
        res = 0
        s_len = len(s)
        if len(s) == 0:
            return True
        
        for i in t:
            if s[current_idx] == i:
                current_idx += 1
                res += 1
            if res == s_len:
                return True
        return False
    


s = "axc"
t = "ahbgdc"
sol = Solution()
print(sol.isSubsequence(s,t))