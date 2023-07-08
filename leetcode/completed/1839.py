class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        appeared = set([ord(word[0])])
        left = 0
        res = 0

        for right in range(1, len(word)):
            if word[right] != word[right-1]:
                for o in appeared:
                    if ord(word[right])-o <= 0:
                        left = right
                        appeared = set()
                        break
                appeared.add(ord(word[right]))

            if len(appeared) == 5:
                res = max(res, right-left+1)

        return res
    
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        appeared = set(word[0])
        left = 0
        res = 0

        for right in range(1, len(word)):
            if word[right] < word[right-1]:
                left = right
                appeared = set()

            appeared.add(word[right])
            if len(appeared) == 5:
                res = max(res, right-left+1)

        return res



sol = Solution()
print(sol.longestBeautifulSubstring("aeiaaioaaaaeiiiiouuuooaauuaeiu"))