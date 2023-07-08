from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        memo = {}
        res = 0

        for word in words:
            memo[word] = memo.get(word, 0) + 1
        for key in memo.keys():
            if memo[key]:
                pair = key[::-1]
                if pair == key:
                    if memo[pair] > 1:
                        res += 4 * (memo[pair] // 2)
                        memo[pair] %= 2
                elif pair in memo:
                    min_ = min(memo[key], memo[pair])
                    res += 4 * min_ 
                    memo[key] -= min_
                    memo[pair] -= min_

        for key in memo.keys():
            if key == key[::-1] and memo[key]:
                res += 2
                break

        return res