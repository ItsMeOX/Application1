from typing import List

# From every index i, we will iterate from i to len(s),
# and if s[i:j+1] is not in dictionary, we will +1 to cost, and we will
# explore what will be the minimum cost starting from index i=j+1.

from functools import cache
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)

        @cache
        def dfs(i):
            if i == len(s):
                return 0

            res = float('inf')
            cost = 0
            for j in range(i, len(s)):
                if s[i:j+1] in dictionary:
                    res = min(res, dfs(j+1))
                else:
                    cost += 1
                    res = min(res, dfs(j+1) + cost)
            
            return res

        return dfs(0)
    
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)

        @cache
        def dfs(i):
            if i == len(s):
                return 0

            res = dfs(i+1) + 1
            for j in range(i, len(s)):
                if s[i:j+1] in dictionary:
                    res = min(res, dfs(j+1))
            
            return res

        return dfs(0)

# Using trie here, reducing O(N^3) to O(N^2).
# Create a trie for the words in dictionary, and we can traverse through
# this trie when we are looping j to i to len(s), so that we do not have to
# make a substring every for every j.
# If we have come to end in the trie, we can also break the j loop more quickly.

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = {}
        for word in dictionary:
            cur_trie = trie
            for char in word:
                if char not in cur_trie:
                    cur_trie[char] = {}
                cur_trie = cur_trie[char]
            cur_trie['*'] = {}

        dp = [len(s)] * (len(s)+1)
        dp[-1] = 0

        for i in range(len(s)-1, -1, -1):
            dp[i] = dp[i+1] + 1
            cur_trie = trie
            for j in range(i, len(s)):
                if s[j] not in cur_trie:
                    break
                cur_trie = cur_trie[s[j]]
                if '*' in cur_trie:
                    dp[i] = min(dp[i], dp[j+1])
        
        return dp[0]
