class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'}':'{', ')':'(', ']':'['}
        stack = []
        cur = 0
        while cur < len(s):
            if s[cur] in brackets:
                if len(stack) <= 0:
                    return False
                if stack[-1] == brackets[s[cur]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[cur])
            cur += 1
        return len(stack) == 0

        