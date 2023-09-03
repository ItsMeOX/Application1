from typing import List

# Initialize 'required' dictionary which stores the minimum required frequency for each letter in word2.
# Note that for example: words1 = 'leetcode', 
#                        words2 = 'lo', 'eo'
# we only need one 'o' instead of 2 'o'. (here 'leetcode' is valid.)
# We then initialize 'total_req' which is total number of characters required to be fulfilled.
# We then iterate through words1 and for each word1, create another counter dictionary for it and
# if cur_count of cur_character == required[cur_charactor], increase 'current_req' by 1.
# If at the end of word iteration, 'current_req' == 'total_req', then append it to 'res' array.

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        required = {}
        res = []

        for word in words2:
            temp = {}
            for c in word:
                temp[c] = temp.get(c, 0) + 1
            for key in temp.keys():
                if key not in required or required[key] < temp[key]:
                    required[key] = temp[key]

        total_req = len(required)

        for word in words1:
            counter = {}
            current_req = 0
            for c in word:
                counter[c] = counter.get(c, 0) + 1
                if c in required and counter[c] == required[c]:
                    current_req += 1
            if current_req == total_req:
                res.append(word)

        return res