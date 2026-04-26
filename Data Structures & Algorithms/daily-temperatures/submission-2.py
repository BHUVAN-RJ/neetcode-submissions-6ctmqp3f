class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            cur = temperatures[i]
            l = i + 1
            days = 1
            while l < len(temperatures) and temperatures[l] <= cur:
                if l == len(temperatures) - 1:
                    days = 0
                    break
                days += 1
                l += 1
            res.append(days)
        res[-1] = 0
        return res
        