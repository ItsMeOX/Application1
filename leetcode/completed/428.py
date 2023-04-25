class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        from collections import defaultdict
        Pdict = defaultdict(int)
        Sdict = defaultdict(int)
        res = []

        for letter in p:
            Pdict[letter] += 1

        right = 0
        left = 0
        len_s = len(s)
        len_p = len(p)
        if len_s < len_p:
            return []
        while right < len_p:
            Sdict[s[right]] += 1
            right += 1
        if Sdict == Pdict:
            res.append(0)
        
        for char in s[right:]:
            
            Sdict[s[left]] -= 1
            if Sdict[s[left]] == 0:
                Sdict.pop(s[left])
            left += 1
            Sdict[char] += 1

            if Pdict == Sdict:
                res.append(left)

        return res    
        
    
sol = Solution()
s = "aa"
p = "aaaaaaaaaa"
print(sol.findAnagrams(s,p))
