from typing import List

# For each word in words, we either take or not take the word.
# 1. If we not take the word, then return dfs(i+1, remain)
# 2. If we take the word, then we check if we can take the word from the remaining letters unused,
#    if we cannot then do nothing,
#    if we can then return dfs(i+1, remain - letters used here) + score.
# Here we keep track of the remaining unused letters by utilizing a counter dictionary.

# TC: O(N * 2^N) ?
# SC: O(N)

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        def getScore(i, dic):
            res = 0
            for c in words[i]:
                if c not in dic:
                    return -1
                dic[c] -= 1
                if not dic[c]: del dic[c]
                res += score[ord(c) - ord('a')]
            return res

        def dfs(i, remain):
            if i == len(words):
                return 0
            
            # skip
            res = dfs(i+1, remain)

            # not skip
            temp = remain.copy()
            score = getScore(i, temp)
            if score != -1:
                res = max(res, score + dfs(i+1, temp))
            
            return res
        
        counter = {}
        for letter in letters:
            counter[letter] = counter.get(letter, 0) + 1

        return dfs(0, counter)