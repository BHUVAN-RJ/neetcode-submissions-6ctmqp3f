class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            if len(stack) == 0:
                stack.append((temperatures[i], i))
                continue
            while len(stack) > 0 and stack[-1][0] < temperatures[i]:
                cur = stack.pop()
                res[cur[1]] = i - cur[1]
            stack.append((temperatures[i], i))
        while len(stack) > 0:
            cur = stack.pop()
            res[cur[1]] = 0
        return res


        