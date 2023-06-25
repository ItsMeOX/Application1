class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        memo = {}
        for i in range(len(s)-minSize+1): # 0 ~ 9-3 (6+1)
            char = set()
            letter_count = 0
            curr_substring = ""
            add_to_memo = True
            for j in range(i, i+minSize):
                if s[j] not in char:
                    letter_count += 1
                    char.add(s[j])
                if letter_count > maxLetters:
                    add_to_memo = False
                    break
                curr_substring += s[j]
            if add_to_memo:
                memo[curr_substring] = memo.get(curr_substring, 0) + 1
        return max(memo.values()) if memo.values() else 0

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        memo = {}
        for i in range(minSize-1, len(s)):
            curr_substring = s[i+1-minSize:i+1]
            if len(set(curr_substring)) <= maxLetters:
                memo[curr_substring] = memo.get(curr_substring, 0) + 1
        
        return max(memo.values()) if memo.values() else 0


sol = Solution()
print(sol.maxFreq(s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3))