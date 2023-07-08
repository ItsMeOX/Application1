class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        dic = {} # to be changed: [change to, cnt]
        swapped = False
        identical = False
        for i in range(len(s)):
            if s[i] == goal[i]:
                if s[i] in dic and s[i] == dic[s[i]][0]:
                    identical = True
                    del dic[s[i]]
                if not identical:
                    dic[s[i]] = [goal[i], 1]


            else:
                if not swapped:
                    if goal[i] in dic and dic[goal[i]][0] == s[i]:
                        swapped = True
                        dic[goal[i]][1] -= 1
                        if not dic[goal[i]][1]:
                            del dic[goal[i]]
                    else:
                        if s[i] in dic:
                            dic[s[i]][1] += 1
                        else:
                            dic[s[i]] = [goal[i], 1]
                else:
                    return False

        return True if (swapped or identical) and all(e == dic[e][0] for e in dic.keys()) else False
    
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        if s == goal:
            dic = {}
            for c in s:    
                dic[c] = dic.get(c, 0) + 1
                if dic[c] >= 2:
                    return True
            return False
        
        indices = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                indices.append(i)

        return len(indices) == 2 and s[indices[0]] == goal[indices[1]] and s[indices[1]] == goal[indices[0]]

