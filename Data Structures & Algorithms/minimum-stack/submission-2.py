class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        '''for i in range(len(self.stack) - 1):
            least = self.stack[i]
            if self.stack[i+1] < self.stack[i]:
                least = self.stack[i+1]
        return least'''

        least = self.stack[0]

        for num in self.stack:
            if num < least:
                least = num
                
        return least
