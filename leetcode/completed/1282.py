from typing import List
from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)

        for i, group in enumerate(groupSizes):
            if not groups[group] or len(groups[group][-1]) == group:
                groups[group].append([])
            groups[group][-1].append(i)
        
        res = []
        for group in groups.values():
            res.extend(group)
            
        return res