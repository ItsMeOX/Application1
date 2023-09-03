from typing import List

# Set up a reversed trie (build trie from end to start of words).
# For every query, append char to self.text and check from end to start of text,
# if end of words is found ('*'), then there is a suffix of self.text, return true,
# else return false.
# Note that we have to check if there is any ending of word after iterating (query method last line).

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.text = ''

        for word in words:
            trie = self.trie
            for i in range(len(word)-1, -1, -1):
                c = word[i]
                if c not in trie:
                    trie[c] = {}
                trie = trie[c]
            trie['*'] = {}



    def query(self, letter: str) -> bool:
        self.text += letter
        trie = self.trie
        for i in range(len(self.text)-1, -1, -1):
            c = self.text[i]
            if '*' in trie:
                return True
            if c not in trie:
                return False
            trie = trie[c]
        
        return '*' in trie





# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)