class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = strs[0]

        for i in range(len(res)):
            for word in strs:
                if i >= len(word) or res[i] != word[i]:
                    return res[:i]
        return res