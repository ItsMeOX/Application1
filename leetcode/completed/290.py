class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pairs = {}
        words = s.split()

        if len(words) != len(pattern): return False

        for i in range(len(words)):
            if pattern[i] in pairs:
                if pairs[pattern[i]] != words[i]:
                    return False
            
            else:
                if words[i] in pairs.values():
                    return False
                pairs[pattern[i]] = words[i]

        return True