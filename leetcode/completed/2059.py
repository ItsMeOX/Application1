from typing import List
from collections import deque

class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        q = deque()
        q.append(start)
        seen = set()
        res = 0

        while q:
            for _ in range(len(q)):
                num = q.popleft()
                if num == goal: return res
                if num > 1000 or num < 0: continue
                for n in nums:
                    if num+n not in seen:
                        seen.add(num+n)
                        q.append(num+n)
                    if num-n not in seen:
                        seen.add(num-n)
                        q.append(num-n)
                    if num^n not in seen:
                        seen.add(num^n)
                        q.append(num^n)
            res += 1
        
        return -1
    
class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        q = deque([start])
        seen = set([start])
        res = 0

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for num in nums:
                    for next_node in [node+num, node-num, node^num]:
                        if next_node == goal: return res + 1
                        if next_node not in seen and 0 <= next_node <= 1000:
                            seen.add(next_node)
                            q.append(next_node)
            res += 1

        return -1

sol = Solution()
print(sol.minimumOperations([2,8,16], 0, 1))