class Solution:
    def finalString(self, s: str) -> str:
        res = ''

        for c in s:
            if c == 'i':
                res = res[::-1]
            else:
                res += c
        
        return res
    
# Can do this in O(n) time using linked list.