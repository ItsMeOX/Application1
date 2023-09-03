from collections import deque

# Perform a BFS from every 'L' and 'R'.
# Cases:
# 1. R.L -> unchange
# 2. R..L -> RRLL
# If neighbour cell is visited, then continue.
# We will mark cell as visited after done iterating thru the whole deque.

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        visited = [False] * n

        dominoes = list(dominoes)
        q = deque()
        for i in range(n):
            if dominoes[i] != '.':
                q.append(i)
                visited[i] = True
        
        while q:
            visiting = set()
            for _ in range(len(q)):
                index = q.popleft()

                if dominoes[index] == 'L' and index > 0 and visited[index-1] == False:
                    visiting.add(index-1)
                    if dominoes[index-1] == '.':
                        dominoes[index-1] = 'L'
                        q.append(index-1)
                    elif dominoes[index-1] == 'R':
                        dominoes[index-1] = '.'
                        visiting.remove(index-1)
                
                if dominoes[index] == 'R' and index < n-1 and visited[index+1] == False:
                    visiting.add(index+1)
                    if dominoes[index+1] == '.':
                        dominoes[index+1] = 'R'
                        q.append(index+1)
                    elif dominoes[index+1] == 'L':
                        dominoes[index+1] = '.'
                        visiting.remove(index+1)
            
            for v in visiting:
                visited[v] = True
    
        return ''.join(dominoes)
    
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        depth = [0] * n

        cur_depth = 0
        for i in range(n-1, -1, -1):
            if dominoes[i] == 'L':
                cur_depth = n
            elif dominoes[i] == 'R':
                cur_depth = 0
            depth[i] += cur_depth
            cur_depth = max(0, cur_depth-1)
        
        cur_depth = 0
        for i in range(n):
            if dominoes[i] == 'R':
                cur_depth = n
            elif dominoes[i] == 'L':
                cur_depth = 0
            depth[i] -= cur_depth
            cur_depth = max(0, cur_depth-1)
        
        

        res = []
        for i in range(n):
            if depth[i] > 0:
                res.append('L')
            elif depth[i] < 0:
                res.append('R')
            else:
                res.append('.')

        return ''.join(res)