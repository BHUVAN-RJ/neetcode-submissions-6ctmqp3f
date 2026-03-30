class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            curTime = 0
            mid = (l + r) // 2
            for i in piles:
                curTime += math.ceil(i / mid)
            print(curTime, res, l, r)
            if curTime <= h:
                r = mid - 1
                res = min(res, mid)
            else:
                l = mid + 1
        return res 