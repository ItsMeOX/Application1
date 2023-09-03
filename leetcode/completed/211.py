class TrieNode:
    
    def __init__(self, isEnd):
        self.isEnd = isEnd
        self.next = {}

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode(False)

    def addWord(self, word: str) -> None:
        trie = self.trie
        for i in range(len(word)):
            c = word[i]
            if c not in trie.next:
                new_node = TrieNode(False) # do not set isEnd here, as this node might already exists and we might not undergo this if statement.
                trie.next[c] = new_node
            if i == len(word)-1: trie.next[c].isEnd = True
            trie = trie.next[c]


    # ------------------------------------
    def search(self, word: str) -> bool:
        def dfs(i, trie):
            if i == len(word): return trie.isEnd

            for key in trie.next: # slow
                if word[i] == '.' or key == word[i]:
                    if dfs(i+1, trie.next[key]): return True
            
            return False

        return dfs(0, self.trie)

    def search(self, word: str) -> bool:
        def dfs(i, trie):
            if i == len(word): return trie.isEnd

            if word[i] == '.': # Optimization: do not loop through the whole dictionary, loop only if the character is '.'
                for key in trie.next:
                    if dfs(i+1, trie.next[key]): return True
            else:
                return word[i] in trie.next and dfs(i+1, trie.next[word[i]])

        return dfs(0, self.trie)
    # ------------------------------------


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# Another optimization using dictionary only:
class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        trie = self.trie
        for i in range(len(word)):
            c = word[i]
            if c not in trie:
                trie[c] = {}
            trie = trie[c]

        # Using '*' as word end marker.
        trie['*'] = {} # do not mark at len - 1, as we might have 'aa.b' after traversing from '.' to next node, we might get True instead of False.
    
    def search(self, word: str) -> bool:
        def dfs(i, trie):
            if i == len(word): return '*' in trie

            if word[i] == '.':
                for key in trie:
                    if dfs(i+1, trie[key]): return True
            
            return word[i] in trie and dfs(i+1, trie[word[i]])
        
        return dfs(0, self.trie)
