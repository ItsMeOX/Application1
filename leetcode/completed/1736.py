class Solution:
    def maximumTime(self, time: str) -> str:
        h1, h2, _, m1, m2 = time

        if h1 == '?':
            if h2 in '456789': h1 = '1'
            else: h1 = '2'
        
        if h2 == '?':
            if h1 == '2': h2 = '3'
            else: h2 = '9'

        if m1 == '?':
            m1 = '5'

        if m2 == '?':
            m2 = '9'
        
        return f'{h1}{h2}:{m1}{m2}'
    
class Solution:
    def maximumTime(self, time: str) -> str:
        time = list(time)

        clock = ['2', '3', ':', '5', '9']
        for i in range(len(time)):
            if time[i] == '?':
                if i == 0 and time[1] != '?' and int(time[1]) > 3:
                    time[0] = '1'
                elif i == 1 and time[0] != '2':
                    time[1] = '9'
                else:
                    time[i] = clock[i]
        
        return ''.join(time)