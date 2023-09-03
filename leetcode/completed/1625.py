from collections import deque

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        seen = set()
        res = s

        def dfs(s):
            nonlocal res
            if s in seen:
                return 

            res = min(res, s)
            seen.add(s)

            temp = ''
            odd = False

            # add
            for c in s:
                if odd:
                    c = str((int(c) + a) % 10)
                odd = not odd
                temp += c
            
            dfs(temp)

            # rotate
            dfs(temp[-b:]+temp[:len(temp)-b])

        dfs(s)

        return res

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        seen = set()
        seen.add(s)
        q = deque()
        q.append(s)
        res = s

        while q:

            # add
            for _ in range(len(q)):
                current = list(q.popleft())
                while True:
                    for i in range(1, len(current), 2):
                        current[i] = str((int(current[i]) + a) % 10)

                    current = ''.join(current)
                    res = min(res, current)

                    if current not in seen:
                        seen.add(current)
                        q.append(current)
                        current = list(current)
                    else:
                        break

            # rotate
            for _ in range(len(q)):
                current = list(q.popleft())

                while True:
                    current = current[-b:] + current[:len(current)-b]

                    current = ''.join(current)
                    res = min(res, current)

                    if current not in seen:
                        seen.add(current)
                        q.append(current)
                        current = list(current)
                    else:
                        break

        return res