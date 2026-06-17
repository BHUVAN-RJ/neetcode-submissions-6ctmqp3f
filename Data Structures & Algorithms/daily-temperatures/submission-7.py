class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if stack:
                # cur temp small than stack top
                # cur temp big than stack top
                while stack and temperatures[i] > stack[-1][0]:
                    val, idx = stack.pop()
                    print(i, idx, res)
                    res[idx] = i - idx
                stack.append((temperatures[i], i))
            else:
                stack.append((temperatures[i], i))
        return res

        