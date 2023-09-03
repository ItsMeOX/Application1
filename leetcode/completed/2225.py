from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = {} # loss

        for win, loss in matches:
            if win not in players:
                players[win] = 0
            if loss not in players:
                players[loss] = 0
            players[loss] += 1
        
        res = [[], []]
        for player in players:
            if players[player] == 0:
                res[0].append(player)
            elif players[player]== 1:
                res[1].append(player)

        res[0].sort()
        res[1].sort()
        return res

