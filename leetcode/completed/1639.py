from typing import List

# Here i = ith character of target,
#      j = jth column of words
#      k = kth row of words.
# Instead of iterating through j columns every i and k,
# we can precompute the frequency of alphabets at every jth column, and multiply frequency of that character at column j.

from functools import lru_cache
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        frequency = [[0]*26 for _ in range(len(words[0]))]
        for i in range(len(words[0])):
            for j in range(len(words)):
                frequency[i][ord(words[j][i]) - ord('a')] += 1


        @lru_cache(None)
        def dfs(i, k): # ith character of target, kth col of words
            if i == len(target):
                return 1
            
            if k == len(words[0]):
                return 0

            # skip current k
            res = dfs(i, k+1)

            # use current k
            for j in range(26):
                if chr(ord('a') + j) == target[i] and frequency[k][j]:
                    res += dfs(i+1, k+1) * frequency[k][j]

            return res % (10 ** 9 + 7)
        
        return dfs(0, 0)
    

class Solution:
    def numWays(self, words: List[str], target: str) -> int:

        frequency = [[0]*26 for _ in range(len(words[0]))]
        for i in range(len(words[0])):
            for j in range(len(words)):
                frequency[i][ord(words[j][i]) - ord('a')] += 1

        dpb = [1] * (len(words[0])+1)

        for i in range(len(target)-1, -1, -1):
            dpf = [0] * (len(words[0])+1)
            for k in range(len(words[0])-1, -1, -1):
                dpf[k] = dpf[k+1]

                # ---------------
                for j in range(26):
                    if chr(ord('a') + j) == target[i] and frequency[k][j]:
                        dpf[k] += (dpb[k+1] * frequency[k][j]) % (10 ** 9 + 7)
            
                # Optimization:
                # instead of loop j from 0 to 25,
                # we can just check if frequency[k][index of character of target[i]] != 0,
                if frequency[k][ord(target[i]) - ord('a')]:
                    dpf[k] += (dpb[k+1] * frequency[k][ord(target[i]) - ord('a')]) % (10 ** 9 + 7)
                # ----------------

            dpb = dpf
        
        return dpf[0] % (10 ** 9 + 7)
