class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        cur_idx = 0
        mapper = {' ': ' '}

        for c in key:
            if c not in mapper:
                mapper[c] = chr(ord('a') + cur_idx)
                cur_idx += 1
        
        res = ''
        for c in message:
            res += mapper[c]
        
        return res