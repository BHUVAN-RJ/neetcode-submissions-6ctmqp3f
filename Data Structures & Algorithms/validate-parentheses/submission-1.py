class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracks = {')':'(', '}':'{', ']':'['}

        for i in s:
            if len(stack) > 0 and i in bracks:
                if bracks[i] == stack[-1]:
                    stack.pop()
                    continue
                else:
                    return False
            stack.append(i)
        return True if len(stack) == 0 else False

        