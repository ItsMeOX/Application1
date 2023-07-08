from collections import deque, defaultdict
from typing import List

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        adjList = defaultdict(list)
        for i in range(len(friends)):
            arr = friends[i]
            for friend in arr:
                adjList[i].append(friend)
        
        visited = set()
        visited.add(id)
        q = deque()
        q.append(id)
        cnt = defaultdict(int)
        

        for k in range(level):
            for _ in range(len(q)):
                people = q.popleft()
                for friend in adjList[people]:
                    if friend not in visited:
                        if k == level-1:
                            for video in watchedVideos[friend]:
                                cnt[video] += 1
                        else:
                            q.append(friend)
                        visited.add(friend)
        
        return sorted(cnt.keys(), key=lambda e: (cnt[e], e))

sol = Solution()
print(sol.watchedVideosByFriends(watchedVideos = [["A","B"],["B", "C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 1))