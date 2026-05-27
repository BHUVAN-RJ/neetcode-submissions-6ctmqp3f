class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brs = {'(':')', '{':'}', '[':']'}
        for p in s:
            if p in brs:
                stack.append(p)
            elif stack and brs[stack[-1]] == p:
                stack.pop()
            else:
                return False
        return len(stack) == 0

        