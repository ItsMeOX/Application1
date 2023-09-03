from collections import defaultdict
from typing import List

# Group string by sorted string then append the array of sorted string to res.
# (can also use counting sort here for the sorting of alphabets.)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) # sorted str: [...strings]

        for i in range(len(strs)):
            string = ''.join(sorted(list(strs[i])))
            groups[string].append(strs[i])
        
        return [res for res in groups.values()]