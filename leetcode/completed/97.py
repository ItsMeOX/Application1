from functools import lru_cache

# Check at every k, if s3[k] == s1[i] or s3[k] == s2[j],
# we will try fitting both characters into s3.
# Once k reaches length of s3 and s1 and s2 are completely used up, return True else return False.

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s3: return True
        if not s1 and not s2: return False

        @lru_cache(None)
        def dfs(i, j, k):
            if k == len(s3):
                if i == len(s1) and j == len(s2):
                    return True
                return False

            if i < len(s1) and s1[i] == s3[k]:
                if dfs(i+1, j, k+1):
                    return True
            
            if j < len(s2) and s2[j] == s3[k]:
                if dfs(i, j+1, k+1):
                    return True
            
            return False
        
        return dfs(0, 0, 0)
    
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False

        @lru_cache(None)
        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True
            
            if i < len(s1) and s1[i] == s3[i+j]:
                if dfs(i+1, j):
                    return True
            
            if j < len(s2) and s2[j] == s3[i+j]:
                if dfs(i, j+1):
                    return True
            
            return False
        
        return dfs(0, 0)
    
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False

        dp = [[False]*(len(s2)+1) for _ in range(len(s1)+1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):

                if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True

                if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True
        
        return dp[0][0]