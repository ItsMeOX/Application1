from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.storage = OrderedDict()
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key in self.storage:
            self.storage.move_to_end(key)
            return self.storage[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.storage[key] = value
        self.storage.move_to_end(key)
        if len(self.storage) > self.capacity:
            self.storage.popitem(False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.storage = {}
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def removeFromList(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insertIntoHead(self, node):
        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node

    def removeFromTail(self):
        if len(self.storage) == 0: return
        tail = self.tail.prev
        del self.storage[tail.key]
        self.removeFromList(tail)

    def get(self, key: int) -> int:
        if key not in self.storage:
            return -1

        node = self.storage[key]
        self.removeFromList(node)
        self.insertIntoHead(node)
        return node.val     

    def put(self, key: int, value: int) -> None:
        if key in self.storage:
            node = self.storage[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            node.val = value
        else:
            if len(self.storage) >= self.capacity:
                self.removeFromTail()
            new_node = Node(key, value)
            self.storage[key] = new_node
            self.insertIntoHead(new_node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)