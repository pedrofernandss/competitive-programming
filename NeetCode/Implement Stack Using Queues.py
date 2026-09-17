class MyStack:

    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.size += 1

    def pop(self) -> int:
        removed_value = self.stack[-1]
        self.stack.pop()
        self.size -= 1
        return removed_value

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return self.size == 0