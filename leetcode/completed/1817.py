from typing import List
from collections import defaultdict

# Initialize a 'UAM' dictionary that which key is userID and value is a set which stores the minutes that user has done an action.
# After adding minutes to each userID set, iterate through values of dictionary and add the length of set of each userID and add it to 'res' array.

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        UAM = defaultdict(set)

        for userID, time in logs:
            UAM[userID].add(time)

        res = [0] * k

        for val in UAM.values():
            res[len(val)-1] += 1
        
        return res