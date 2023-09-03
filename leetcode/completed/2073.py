from typing import List
from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        q = deque()
        
        for i in range(len(tickets)):
            q.append((i, tickets[i]))
        
        while q:
            res += 1
            i, ticket_left = q.popleft()
            if ticket_left - 1 != 0:
                q.append((i, ticket_left-1))
            elif i == k:
                return res

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        
        for i in range(len(tickets)):
            if i <= k:
                res += min(tickets[i], tickets[k])
            else:
                res += min(tickets[i], tickets[k] - 1)

        return res