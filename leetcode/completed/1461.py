# For binary code of length k, the total number of unique code will be
# 2^k.
# We can iterate i from 0 to len(s)-k, and check how many unique substrings
# are there of length k. (s[i:i+k])
# If the number of unique substring == 2^k, return True.

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        substr = set()
        for i in range(len(s)-k+1):
            substr.add(s[i:i+k])
        
        return len(substr) == 1 << k
    
sol = Solution()
print(sol.hasAllCodes(s = "0110", k = 2))