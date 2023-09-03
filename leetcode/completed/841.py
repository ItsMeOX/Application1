from collections import deque
from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque()
        q.append(0)
        visited = [False]* len(rooms)
        visited[0] = True

        while q:
            key = q.popleft()
            for room in rooms[key]:
                if not visited[room]:
                    visited[room] = True
                    q.append(room)
        
        return all(visited)
    
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)
        def dfs(key):
            for room in rooms[key]:
                if room not in visited:
                    visited.add(room)
                    dfs(room)
        dfs(0)

        return len(visited) == len(rooms)