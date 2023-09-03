
# Using DP here, which has two states: i is the ith character, last is the corresponding index of current character in ('a', 'e', 'i', 'o', 'u').
# Base case: 1. i == n, return 1, as we have found a way to build the sorted vowel string.
#            2, last == 5, which means the character is 'u', and there is only one possibility which is '..uuuuu..' all the way down to i == n.

class Solution:
    def countVowelStrings(self, n: int) -> int:

        memo = {}

        def dfs(i, last):
            if (i, last) in memo:
                return memo[(i, last)]

            if i == n or last == 5:
                return 1
            
            res = 0
            for j in range(last, 6):
                res += dfs(i+1, j)
            
            memo[(i, last)] = res

            return res
        
        return dfs(0, 1)