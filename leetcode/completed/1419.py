
# Initialize a counter which stores the characters of active croak at the moment.

# If character == 'c', we will check how many frogs are croaking at the moment
# by summing up the values of c,r,o,a (exclude k because k means the frog has done croaking).

# To check if the croaking string is valid or not, we can check the sequence of characters,
# for example,
# if we encounter the character 'r', then we must have atleast one active character 'c', else return -1.
# For every character, we will deduct the counter of prev character by 1 and inc the counter of current character by 1.

# At last, we have to check if counter['c,r,o,a'] are all zero.
# As 'croakcroa' is a invalid string.

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        counter = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}
        prev_chr = {'r': 'c', 'o': 'r' , 'a': 'o' , 'k': 'a'}
        res = 0

        for c in croakOfFrogs:
            
            if c in prev_chr:
                if counter[prev_chr[c]] == 0: return -1
                counter[prev_chr[c]] -= 1
            
            counter[c] += 1

            if c == 'c':
                res = max(res, sum(counter.values())-counter['k'])

        return res if sum(counter.values())-counter['k'] == 0 else -1 # check counter['c,r,o,a'] are all zero.