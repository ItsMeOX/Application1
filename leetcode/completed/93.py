from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        def dfs(i, cur_str, dot_cnt):
            # more than 3 dots or i > len(s), invalid.
            if dot_cnt > 4 or i > len(s): return

            # valid ip (3 dots and digit chunks < 256).
            if i == len(s):
                if dot_cnt == 4:
                    res.append(cur_str[:-1])
                return

            # if digit is 0, then we can only take it as leading zero is not allowed.
            if s[i] == '0':
                dfs(i+1, cur_str + '0' + '.', dot_cnt + 1)
                return


            # take digits chunk of size 1 ~ 3 and add '.' 
            for delta in range(1, 4):
                if int(s[i:i+delta]) > 255: continue
                dfs(i+delta, cur_str + s[i:i+delta] + '.', dot_cnt + 1)

        res = []
        dfs(0, '', 0)
        return res