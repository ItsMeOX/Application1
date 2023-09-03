from collections import defaultdict

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        words = defaultdict(list)
        visited = set()

        for word in wordDict:
            words[word[0]].append(word)
        
        def dfs(i):
            if i in visited:
                return False

            if i == len(s):
                return True
            
            if s[i] not in words:
                return False
            else:
                for word in words[s[i]]:
                    if s[i:i+len(word)] == word and dfs(i+len(word)):
                        return True
            
            visited.add(i)

            return False
        
        return dfs(0)
    
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        
        return dp[-1]