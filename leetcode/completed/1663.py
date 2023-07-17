class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        head = []
        tail = []

        while k > 25:
            head.append(26)
            k -= 26
        
        if len(head) < n and k:
            head.append(k)
            k = 0


        while len(head) + len(tail) < n:
            if head[-1] == 1:
                head.pop()
            else:
                head[-1] -= 1
            tail.append(1)

        head.reverse()

        res = ""

        for c in tail:
            res += chr(c+96)

        for c in head:
            res += chr(c+96)
        
        return res


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = ['a'] * n
        k -= n

        for i in range(n-1, -1, -1):
            if k > 25:
                res[i] = 'z'
                k -= 25
            else:
                res[i] = chr(96 + k+1)
                return "".join(res)

sol = Solution()
print(sol.getSmallestString(n=21, k=416))