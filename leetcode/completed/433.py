from typing import List
from collections import deque

# Here we have to make sure that we change our character one by one and the intermediate string should be in bank.
# We take startGene as current gene, we find if a word in bank has one character difference compared to current gene,
# if yes then we traverse to the word.
# Every time we change a character, we add 1 to res.
# If we ever reach endGene, then return res.
# If we never reached endGene, then return -1.

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        visited = set()
        q = deque([startGene])
        res = 0

        def countDiff(s1, s2):
            diff = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff += 1
            return diff

        while q:
            for _ in range(len(q)):
                gene = q.popleft()

                if gene == endGene: return res

                for mutation in bank:
                    if mutation not in visited and countDiff(gene, mutation) == 1:
                        visited.add(mutation)
                        q.append(mutation)

            res += 1

        return -1