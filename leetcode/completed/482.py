class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res = ''
        i = len(s)
        s = s.replace('-', '').upper()        

        for i in range(len(s)-k, 0, -k):
            res = '-' + s[i:i+k] + res

        res = s[:i] + res

        return res        
    
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res = ''
        s = s.replace('-', '').upper()       
        res = s[:len(s)%k] 
        if res:
            res += '-'

        for i in range(len(s)%k, len(s), k):
            res += s[i:i+k] + '-'

        return res[:-1]