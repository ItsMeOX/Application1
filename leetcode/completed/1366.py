from typing import List

# Initialize an array [0] * 26 for each alphabet, then loop through votes and add 1 to the respective position of the voted index to rank[alphabet].
# The dictionary will look like:
# {
# 'A': [5, 0, 0, 0], 
# 'B': [0, 2, 3, 0], 
# 'C': [0, 3, 2, 0]
# }
# after sorted at decreasing order, the keys will be [A,C,B].
# If two arrays are the same, we then sort it alphabetically using 'ord' function.

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        rank = {}

        for vote in votes:
            for i, team in enumerate(vote):
                if team not in rank:
                    rank[team] = [0] * (len(vote)+1)
                rank[team][i] += 1
        
        res = ''
        for alp in sorted(rank.keys(), key = lambda e: (rank[e], -ord(e)), reverse = True):
            res += alp

        return res