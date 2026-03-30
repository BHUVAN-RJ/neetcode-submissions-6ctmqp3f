# stack = [3]

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for cur in tokens:
            if cur in operators:
                numTwo = stack.pop()
                numOne = stack.pop()
                cur = int(eval(f"{numOne}{cur}{numTwo}"))
            stack.append(cur)
        return int(stack.pop())