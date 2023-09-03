from heapq import heappop, heappush
from typing import List

# Initialize a dictionary which key is friend id and value is the id of chair the friend is occupying.
# Initialize a heap 'chair_available', which stores chair id if someones leaves.
# Initialize and sort arrays 'arrival' and 'leaving' which format is (time arrival/leaving, friend id).
# Iterate through 'arrival' array and 
# 1. check if there is leaving time that is <= arrival time, if yes then get the id of leaving friend and get the id of chair occupied by them
#    through 'chair' dictionary, and append the chair id to 'chair_available' heap.
# 2. check if 'chair_available' has chair id, if yes then assign current arrived friend to the smallest chair id possible.
#                                             if no  then assign current arrived friend to latest chair id.
# Check if current arrival friend is our target friend, if yes then return the id of chair they are assigned to.

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        chair = {} # friend_id: chair_id
        chair_available = [] # chair available if someone leaves
        latest_id = 0

        arrival = sorted([(times[i][0], i) for i in range(len(times))])
        leaving = sorted([(times[i][1], i) for i in range(len(times))])
        j = 0

        for time, friend in arrival:
            while j < len(leaving) and leaving[j][0] <= time:
                heappush(chair_available, chair[leaving[j][1]])
                j += 1
            
            if chair_available:
                chair_id = heappop(chair_available)
            else:
                chair_id = latest_id
                latest_id += 1

            chair[friend] = chair_id

            if friend == targetFriend:
                return chair[friend]