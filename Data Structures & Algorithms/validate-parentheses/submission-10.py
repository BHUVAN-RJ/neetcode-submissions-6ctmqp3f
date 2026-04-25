class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(' : ')', '{' : '}', '[':']'}
        for i in s:
            if i in brackets:
                stack.append(i)
            else:
                if len(stack) > 0 and brackets[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
        