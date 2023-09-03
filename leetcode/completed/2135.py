from typing import List

# Because that the word length is only 26, we can take advantage of this.
# As we are able to know the original word from the constructed word by eliminating one character from the constructed word, we can loop through and remove the character of constructed word one by one and find if the original word exists in startWords.
# To do this, we will sort every startWords and every targetWords, 
# we will store every startWords in a set so we can achieve O(1) search for every targetWords.

class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        res = 0
        startWords = set(''.join(sorted(word)) for word in startWords)

        for word in targetWords:
            word = ''.join(sorted(word))
            for i in range(len(word)):
                substr = word[:i] + word[i+1:]
                if substr in startWords:
                    res += 1
                    break

        return res