class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {'+', '-', '/', '*'}
        for token in tokens:
            if token in op:
                second = int(stack.pop())
                first = int(stack.pop())
                cur = None
                if token == '+':
                    cur = first + second
                elif token == '-':
                    cur = first - second
                elif token == '*':
                    cur = first * second
                else:
                    cur = first / second
                stack.append(cur)
            else:
                stack.append(token)
        return int(stack.pop())

        