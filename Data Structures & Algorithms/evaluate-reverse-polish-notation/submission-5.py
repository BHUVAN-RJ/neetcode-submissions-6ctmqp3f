class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = ['+', '-', '*', '/']
        stack = []
        for token in tokens:
            if token in op:
                oprnd2 = stack.pop()
                oprnd1 = stack.pop()
                stack.append(int(eval(f"{oprnd1}{token}{oprnd2}")))
            else:
                stack.append(token)
        return int(stack.pop())


        