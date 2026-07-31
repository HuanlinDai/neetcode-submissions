class MinStack:

    def __init__(self):
        self.prefix = []
        self.stack = []

    def push(self, val: int) -> None:

        if len(self.prefix) > 0:
            self.prefix.append(min(self.prefix[-1],val))
        else:
            self.prefix.append(val)
        self.stack.append(val)

        return None
        
    def pop(self) -> None:

        self.prefix.pop(-1)
        self.stack.pop(-1)

        return None

    def top(self) -> int:

        return self.stack[-1]

    def getMin(self) -> int:

        return self.prefix[-1]
