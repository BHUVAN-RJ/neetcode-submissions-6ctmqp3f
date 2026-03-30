class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        res = max(piles)
        l, r = 1, max(piles)

        while l <=r:
            curTime = 0
            m = (r+l) // 2
            for i in piles:
                curTime += math.ceil(i / m)

            if curTime > h:
                l = m + 1
            else:
                res = min(res, m)
                r = m - 1
        return res
        