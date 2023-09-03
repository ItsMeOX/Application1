from typing import List

# From current index i, we define our current substring to be in [i, j].
# if s[i ~ j] == reversed( s[i ~ j] ), then we append it to 'cur' and move i to j+1.
# After exploring all the other possibilites after j, we pop current substring from 'cur' and continue increasing j and find other possibilies.

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(i, cur):
            if i == len(s):
                res.append(cur.copy())
                return
            
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    cur.append(s[i:j+1])
                    dfs(j+1, cur)
                    cur.pop()

        dfs(0, [])
        return res