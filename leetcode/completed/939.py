from typing import List
from collections import defaultdict

# Initialize a dictionary which key is X, and value is a list of Y on X. {x: [y1, y2..]}
# Then choose 2 Xs from key of dictionary and check if a Y point exists in both of values of 2 Xs.
# If true then append it to a temporary list (y_list here).
# After checking all Y for 2 Xs, we sort the Y values in the list, 
# and check for the smallest possible delta Y.
# Then we update 'res' with the smallest rectangular area possible.

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        res = float('inf')
        group = defaultdict(list)

        for x, y in points:
            group[x].append(y)
        
        keys = list(group.keys())

        for i in range(len(keys)):
            x1 = keys[i]
            for j in range(i+1, len(keys)):
                x2 = keys[j]
                y_list = []
                smallest_y = float('inf')
                for y in group[x1]:
                    if y in group[x2]:
                        y_list.append(y)
                if len(y_list) < 2: continue # If there is only one point, skip.
                y_list.sort()
                for k in range(len(y_list)-1):
                    smallest_y = min(smallest_y, y_list[k+1]-y_list[k])
                res = min(res, smallest_y * abs(x2-x1)) # Get area.
        
        return res if res < float('inf') else 0