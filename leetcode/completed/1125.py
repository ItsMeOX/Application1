from typing import List

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skill_id = {}

        for i, skill in enumerate(req_skills):
            skill_id[skill] = i

        person_skill_mask = [0] * len(people)

        for i in range(len(people)):
            for skill in people[i]:
                person_skill_mask[i] |= 1 << skill_id[skill]

        memo = {}

        def dfs(i, skill_mask):
            if (i, skill_mask) in memo:
                return memo[(i, skill_mask)]

            if not skill_mask: # all required skills are fulfilled
                return []

            if i == len(people): # invalid combination
                return [0] * 60

            if skill_mask & person_skill_mask[i] == 0: # if all of the skills of the people are included, skip this person
                return dfs(i+1, skill_mask)

            res = min(dfs(i+1, skill_mask), [i] + dfs(i+1, skill_mask & ~person_skill_mask[i]), key=len)
            memo[(i, skill_mask)] = res
            return res


        return dfs(0, (1 << len(req_skills)) - 1)