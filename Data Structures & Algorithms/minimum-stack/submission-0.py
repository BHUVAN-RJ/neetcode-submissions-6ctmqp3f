class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        curMin = self.minStack[-1] if len(self.minStack) else float('inf')
        if curMin < val:
            self.minStack.append(curMin)
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
