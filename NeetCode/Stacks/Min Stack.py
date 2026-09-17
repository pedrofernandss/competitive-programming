class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = math.inf

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.min_value:
            self.min_value = math.inf
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        self.min_value = min(self.stack)
        return self.min_value