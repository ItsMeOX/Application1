from random import randint

# Initialize two dictionary, 
# one is val -> index,
# another one is index -> val.
# Also initialize index, which is the latest index to insert for two dictionaries.

# For insertion,
# mapper:  current value -> current index
# indices: current index -> current value

# For remove,
# find index from indices, delete both index and value from two dictionary.
# If removed index is latest index (index - 1), then do nothing.
# Otherwise, update the latest index and value to the deleted slot.
# Then latest index -= 1.

class RandomizedSet:

    def __init__(self):
        self.index = 0
        self.mapper = {} # val: index 
        self.indices = {} # index: val

    def insert(self, val: int) -> bool:
        if val in self.mapper: return False
        self.mapper[val] = self.index
        self.indices[self.index] = val
        self.index += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.mapper: return False
        index = self.mapper[val]
        del self.indices[index]
        del self.mapper[val]

        if index != self.index - 1:
            self.indices[index] = self.indices[self.index-1]
            self.mapper[self.indices[self.index-1]] = index
            del self.indices[self.index-1]

        self.index -= 1

        return True

    def getRandom(self) -> int:
        return self.indices[randint(0, len(self.indices)-1)]

# Using list instead of 'mapper' dictionary,
# Every remove, just delete the last element of list and update it to
# the slot of the removed element.

class RandomizedSet:

    def __init__(self):
        self.data = []
        self.indices = {} # val: index

    def insert(self, val: int) -> bool:
        if val in self.indices: return False
        self.data.append(val)
        self.indices[val] = len(self.data)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices: return False
        index, last_elm = self.indices[val], self.data[-1]
        self.data[index] = last_elm
        self.indices[last_elm] = index
        self.data.pop()
        del self.indices[val]
        return True

    def getRandom(self) -> int:
        return self.data[randint(0, len(self.data)-1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()