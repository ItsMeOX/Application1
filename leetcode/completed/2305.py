from typing import List

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        if k == len(cookies):
            return max(cookies)

        children = [0] * k
        res = float('inf')

        def check(i):
            nonlocal res
            if i == len(cookies):
                return

            for j in range(k):
                children[j] += cookies[i]
                check(i+1)
                if i == len(cookies)-1:
                    res = min(res, max(children))
                children[j] -= cookies[i]
                
        check(0)
        return res


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        if k == len(cookies):
            return max(cookies)

        children = [0] * k
        res = float('inf')

        def check(i):
            nonlocal res
            if i == len(cookies) or max(children) >= res:
                return
            
            for j in range(k):
                children[j] += cookies[i]
                check(i+1)
                if i == len(cookies)-1:
                    print(children)
                    res = min(res, max(children))
                children[j] -= cookies[i]
        
        check(0)
        return res

        
sol = Solution()
print(sol.distributeCookies(cookies = [8,15,10,20,8], k = 2))