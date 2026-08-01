class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:

        self.array[i] = n
        return None

    def pushback(self, n: int) -> None:
        if self.capacity == self.size:
            self.resize()
        self.array[self.size] = n
        self.size += 1
        return None

    def popback(self) -> int:
        self.size -= 1
        res = self.array[self.size]
        self.array[self.size] = None
        return res

    def resize(self) -> None:
        self.array += [None] * self.capacity
        self.capacity *= 2
        return None

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity