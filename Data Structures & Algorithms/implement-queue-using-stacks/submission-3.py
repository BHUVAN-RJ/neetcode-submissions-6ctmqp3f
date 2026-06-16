class MyQueue:

    def __init__(self):
        self.stack = []
        self.reverse = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        if not self.reverse:
            while self.stack:
                self.reverse.append(self.stack.pop())
        return self.reverse.pop()

        

    def peek(self) -> int:
        if not self.reverse:
            while self.stack:
                self.reverse.append(self.stack.pop())
        return self.reverse[-1]
        

    def empty(self) -> bool:
        if not self.stack and not self.reverse:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

#[1,2,3,4,5]
#[5,4,3,2,1,]