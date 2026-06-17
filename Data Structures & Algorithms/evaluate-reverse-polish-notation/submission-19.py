class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '*', '-', '/']
        stack = []
        for token in tokens:
            if token in operators:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(int(eval(f'{op1}{token}{op2}')))
                continue
            stack.append(int(token))
        return stack.pop()
        