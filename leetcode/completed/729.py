class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.events:
            if start < e and end > s:
                return False
        
        self.events.append((start, end))

        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node(start, end)
            return True
        else:
            return self.traverse(self.root, start, end)
    
    def traverse(self, node, start, end) -> bool:
        if start >= node.end:
            if not node.right:
                node.right = Node(start, end)
                return True
            else:
                return self.traverse(node.right, start, end)
        elif end <= node.start:
            if not node.left:
                node.left = Node(start, end)
                return True
            else:
                return self.traverse(node.left, start, end)
        else:
            return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)