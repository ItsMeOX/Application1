class MyCalendarThree:

    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> int:
        # form a event timeline
        # if start, event += 1
        # if end, event -= 1
        self.events.append((startTime, 1))
        self.events.append((endTime, -1))
        self.events.sort()

        res = temp = 0
        for _, i in self.events:
            temp += i
            res = max(res, temp)

        return res
        

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)

sol = MyCalendarThree()
x = [[26,35],[26,32],[25,32],[18,26],[40,45],[19,26],[48,50],[1,6],[46,50],[11,18]]
for l , h in x:
    sol.book(l, h)
