import heapq
class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        score2 = [-i for i in score]
        heapq.heapify(score2)
        mapping = {}
        i = 1
        while score2:
            mapping[-heapq.heappop(score2)] = i
            i += 1

        for i in range(len(score)):
            if mapping[score[i]] == 1:
                score[i] = "Gold Medal"
            elif mapping[score[i]] == 2:
                score[i] = "Silver Medal"
            elif mapping[score[i]] == 3:
                score[i] = "Bronze Medal"
            else:
                score[i] = f"{mapping[score[i]]}"

        return score

class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        score2 = sorted(score, key=lambda e:-e)
        mapping = {}
        for i in range(len(score2)):
            mapping[score2[i]] = i+1
        
        for i in range(len(score)):
            if mapping[score[i]] == 1:
                score[i] = "Gold Medal"
            elif mapping[score[i]] == 2:
                score[i] = "Silver Medal"
            elif mapping[score[i]] == 3:
                score[i] = "Bronze Medal"
            else:
                score[i] = str(mapping[score[i]])

        return score

sol = Solution()
print(sol.findRelativeRanks([10,3,8,9,4]))