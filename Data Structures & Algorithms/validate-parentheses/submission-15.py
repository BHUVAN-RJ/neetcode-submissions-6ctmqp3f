class Solution:
    def isValid(self, s: str) -> bool:
        brkt = {'[':']', '{':'}', '(':')'}
        stack = []
        for cur in s:
            print
            if cur in brkt:
                stack.append(cur)
            elif stack and brkt[stack[-1]] == cur:
                stack.pop()
            else:
                return False
        return len(stack) == 0
        