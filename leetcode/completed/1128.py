from typing import List

# we can classify (a, b) and (b, a) as the same domino by swapping a and b if b > a
# we initialize a dictionary where key is the pair of domino (a, b) and value is the number of domino seen before the time of current discovery
# for every type of domino, the number of pair formed will be sum of number of domino seen before the time of current discovery
# for example, 
# if we see the type of domino third time, n. of pair that can be formed currently will be n. of domino seen previously, which is 2
# every time we see a domino, the number of pair of domino will be n. of domino seen prev, so res = res + domino seen prevly.

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        record = {}

        res = 0

        for a, b in dominoes:
            if b > a:
                a, b = b, a
            
            if (a, b) not in record:
                record[(a, b)] = 0
            else:
                record[(a, b)] += 1
                
            res += record[(a, b)]

        return res