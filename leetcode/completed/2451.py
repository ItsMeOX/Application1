from typing import List

# Check first three words,
# if count of any word is 1, then it is the answer.
# Else, take a reference of the word and continue checking.
# Continue iterating,
# if we found a string that does not match the difference pattern, then it is the answer.

class Solution:
    def oddString(self, words: List[str]) -> str:
        word_len = len(words[0])
        counter = []
        for i in range(3):
            cur_count = [ord(words[i][j])-ord(words[i][j-1]) for j in range(1, word_len)]
            counter.append(cur_count)

        for i in range(3):
            cur_count = 1
            for j in range(3):
                if i != j and counter[i] == counter[j]:
                    cur_count += 1
            if cur_count == 1:
                return words[i]
            
        reference = counter[0]

        for i in range(len(words)):
            cur_count = [ord(words[i][j])-ord(words[i][j-1]) for j in range(1, word_len)]
            if cur_count != reference:
                return words[i]
