class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int: # didn't notice s1 and s2 contains only x and y, this works for any alphabets
        digit_counter = {}
        total_counter = {}

        for i in range(len(s1)):
            if s1[i] == s2[i]: continue
            digit_counter[s1[i]] = digit_counter.get(s1[i], 0) + 1
            digit_counter[s2[i]] = digit_counter.get(s2[i], 0) + 1
            total_counter[(s1[i], s2[i])] = total_counter.get((s1[i], s2[i]), 0) + 1

        for key in digit_counter.keys():
            if digit_counter[key] & 1:
                return -1

        res = 0
        for key in total_counter.keys():
            res += total_counter[key] // 2
            total_counter[key] %= 2
            res += total_counter[key]

        return res

# observation:
# if number of xy pair or yx pair is even, we can swap one of them and achieve same string, so add 1 to res
# if number of xy pair of yx pair is odd, we need to swap both of xy and yx to achieve same string, so add 2 to res 
# if number of xy pair + number of yx pair is odd number, there will eventually be one left out that is unswapped, 
# that means we are unable to swap to achieve same string, so return -1

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x_y = 0
        y_x = 0

        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                if c1 == 'x':
                    x_y += 1
                else:
                    y_x += 1

        if (x_y + y_x) % 2 == 1:
            return -1

        return (x_y // 2 + x_y % 2) + (y_x // 2 + y_x % 2)