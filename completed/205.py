from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        check = defaultdict(set)
        check2 = defaultdict(set)
        for idx, cha in enumerate(s):
            check[cha].add(t[idx])
            check2[t[idx]].add(cha)

            if len(check[cha]) > 1 or len(check2[t[idx]]) > 1:
                return False
        return True
            
s = "badc"
t = "baba"

sol = Solution()
print(sol.isIsomorphic(s,t))