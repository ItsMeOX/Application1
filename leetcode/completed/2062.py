class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        res = 0
        for i in range(len(word)-4):
            cur_set = set()
            for j in range(i, len(word)):
                cur_set.add(word[j])
                if len(cur_set) > 5: break
                if all(v in cur_set for v in 'aeiou'):
                    res += 1

        return res
    
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        lastVowel = {v:-1 for v in 'aeiou'}
        lastNormal = -1
        res = 0

        for i in range(len(word)):
            if word[i] not in lastVowel:
                lastNormal = i
            else:
                lastVowel[word[i]] = i
                res += max(0, min(lastVowel.values()) - lastNormal) 

        return res