from typing import List
from collections import defaultdict

# Take first element of adjacentPairs as starting pair.
# Create a dictionary where its key is head/tail and its value are neighbour alphabets.
# Example: [a, b] => we store this pair as: dict[a] = [b], dict[b] = a.
# Start iterating from second element of adjacentPairs, find and append neighbour alphabet to dictionary.
# Iterate from right of starting pair, append neighbour alphabet to the res list.
# We have to check if we have used the same pair by adding reversed pair to seen.
# After done iterating on right side, do the same thing for the left side by reversing the res list and reiterate.

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        res = adjacentPairs[0]
        pair = defaultdict(list)
        seen = set()

        for i in range(1, len(adjacentPairs)):
            x, y = adjacentPairs[i]
            pair[x].append(y)
            pair[y].append(x)

        while res[-1] in pair:
            if not pair[res[-1]]:
                del pair[res[-1]]
            else:
                cur_num = pair[res[-1]].pop()
                if cur_num not in seen:
                    seen.add(res[-1])
                    res.append(cur_num)

        res.reverse()

        while res[-1] in pair:
            if not pair[res[-1]]:
                del pair[res[-1]]
            else:
                cur_num = pair[res[-1]].pop()
                if cur_num not in seen:
                    seen.add(res[-1])
                    res.append(cur_num)

        return res
    
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        res = adjacentPairs[0]
        pair = defaultdict(list)

        for i in range(1, len(adjacentPairs)):
            x, y = adjacentPairs[i]
            pair[x].append(y)
            pair[y].append(x)

        while res[-1] in pair:
            prev = res[-2]      # no need to add reversed pair to seen, just check if newly added alphabet is same second last element of list or not.
            if not pair[res[-1]]:
                del pair[res[-1]]
            else:
                cur_num = pair[res[-1]].pop()
                if cur_num != prev:
                    res.append(cur_num)

        res.reverse()

        while res[-1] in pair:
            prev = res[-2]
            if not pair[res[-1]]:
                del pair[res[-1]]
            else:
                cur_num = pair[res[-1]].pop()
                if cur_num != prev:
                    res.append(cur_num)

        return res
    
# Optimization:
# There will be starting/ending alphabet that the length of adjacent alphabet is only 1.
# We can find that start iterating from there, so that we do not need to reverse the list.
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        pair = defaultdict(list)
        seen = set()

        for i in range(len(adjacentPairs)):
            x, y = adjacentPairs[i]
            pair[x].append(y)
            pair[y].append(x)

        for key in pair.keys():
            if len(pair[key]) == 1:
                res = [key]
                seen.add(key)
                break

        while res[-1] in pair:
            if not pair[res[-1]]:
                del pair[res[-1]]
            else:
                cur_num = pair[res[-1]].pop()
                if cur_num not in seen:
                    res.append(cur_num)
                    seen.add(cur_num)

        return res