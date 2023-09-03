class Solution:
    def entityParser(self, text: str) -> str:
        mapper = {
            '&quot;': ['"'],
            '&apos;': ["'"],
            '&amp;' : ['&'],
            '&gt;'  : ['>'],
            '&lt;'  : ['<'],
            '&frasl;': ['/'],
        }

        text = list(text)
        left = 0
        for right in range(len(text)):
            if text[right] == '&': left = right
            if text[right] == ';' and ''.join(text[left: right+1]) in mapper:
                text[left: right+1] = mapper[''.join(text[left: right+1])] + [''] * (right-left)
                left += 1

        return ''.join(text)
    
# Have to put &amp; at last, in case of '&amp;amp;'.

class Solution:
    def entityParser(self, text: str) -> str:
        mapper = {
            '&quot;': '"',
            '&apos;': "'",
            '&gt;'  : '>',
            '&lt;'  : '<',
            '&frasl;': '/',
            '&amp;' : '&',
        }

        for key in mapper:
            text = text.replace(key, mapper[key])

        return text