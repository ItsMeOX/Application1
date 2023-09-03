from typing import List

# Sort the words by their lengths first, then iterate through every word in words,
# check if word can be built by concatenating words in trie,
# here if we reach end of word, we can jump back to head of trie,
# or we can continue checking.
# If cannot be built by conatenating then build up trie with the word.

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key = len)
        self.trie = {}
        res = []

        def canConcat(i, word, trie):
            if i == len(word):
                return '*' in trie

            if word[i] in trie and canConcat(i+1, word, trie[word[i]]): return True
            if '*' in trie and canConcat(i, word, self.trie): return True

            return False

        def build(word):
            trie = self.trie
            for c in word:
                if c not in trie:
                    trie[c] = {}
                trie = trie[c]
            trie['*'] = {}

        for word in words:
            if canConcat(0, word, self.trie):
                res.append(word)
            else:
                build(word)
        
        return res