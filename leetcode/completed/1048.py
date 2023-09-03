from typing import List

# Here we will start from every words[i] in words for i in range [0, words.length-1],
# then from each words, we will check all the words[j] which
# 1. j > i
# 2. words[j].length == words[i].length + 1
# 3. words[i] is predecessor of words[j]

# Here we can check if words[i] is predecessor of words[j] by checking 
# words1[different index:] == words2[different index+1:], if true then word1 is predecessor of word2.
# For example, word1 = "bda", word2 = "bdca",
# different index = 2
# word1[2:] == a == word2[2+1:] == a
# so word1 is predecessor of word2.

from functools import cache
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = len)

        def ispredecessor(word1, word2):
            for i in range(min(len(word1), len(word2))):
                if word1[i] != word2[i]:
                    return word1[i+1:] == word2[i:] or word1[i:] == word2[i+1:]
            return True

        @cache
        def dfs(i):
            res = 0
            for j in range(i+1, len(words)):
                if len(words[j]) == len(words[i])+1:
                    if ispredecessor(words[i], words[j]):
                        res = max(res, dfs(j) + 1)

            return res
        
        res = 0
        for i in range(len(words)):
            res = max(res, dfs(i) + 1)
        
        return res
    
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = len)

        def ispredecessor(word1, word2):
            for i in range(min(len(word1), len(word2))):
                if word1[i] != word2[i]:
                    return word1[i+1:] == word2[i:] or word1[i:] == word2[i+1:]
            return True
        
        dp = [1] * len(words)

        for i in range(len(words)-1, -1, -1):
            for j in range(i+1, len(words)):
                if len(words[j]) == len(words[i])+1 and ispredecessor(words[i], words[j]):
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
    
# Instead of N^2 * len(words[i]), we can do len(words[i])^2 * N.
# For each words, if we removed a character and the word exists before words[i],
# we will update dic[words[i]] = max(dic[words[i]], dic[removed_char_word] + 1).

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = len)
        word_dic = {}
        
        for word in words:
            if word not in word_dic:
                word_dic[word] = 1
            for j in range(len(word)):
                pre = word[:j] + word[j+1:]
                if pre in word_dic:
                    word_dic[word] = max(word_dic[word], word_dic[pre] + 1)
        
        return max(word_dic.values())