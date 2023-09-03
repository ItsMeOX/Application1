from typing import List

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == 'type': idx = 0
        elif ruleKey == 'color': idx = 1
        else: idx = 2
        res = 0

        for item in items:
            if item[idx] == ruleValue:
                res += 1
            
        return res
    
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        mapper = {'type': 0, 'color': 1, 'name': 2}
        res = 0

        for item in items:
            if item[mapper[ruleKey]] == ruleValue:
                res += 1
            
        return res