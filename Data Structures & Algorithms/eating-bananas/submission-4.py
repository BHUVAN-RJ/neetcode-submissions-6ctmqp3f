class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
       l, r = 1, max(piles)
       
       res = r
       while l <= r:
            curTime = 0
            m = (l+r) // 2
            for i in piles:
                curTime += math.ceil(i/m)
            if curTime <= h:
                r = m - 1
                res = min(res, m)
            else:
                l = m + 1
       return res

