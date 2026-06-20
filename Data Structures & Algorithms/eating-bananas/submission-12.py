# l = 1, r = 25 -- m = 13
# [25,10,23,4] ceil / = 2 + 1 + 2 + 1 = 6 -> invalid
# l = 14, r = 25 -- m = 19
# [25,10,23,4] ceil / = 2 + 1 + 2 + 1 = 6 -> invalid
# l = 20, r = 25 -- m = 22
# [25,10,23,4] ceil / = 2 + 1 + 2 + 1 = 6 -> invalid
# l = 23, r = 25 -- m = 24
# [25,10,23,4] ceil / = 2 + 1+ 1+1 = 5 --> invalid
# l = 25, r = 25 -- m = 25
# [25,10,23,4] ceil / = 1 + 1 + 1 + 1 = 4 --> valid


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = float('inf')
        while l <= r:
            mid = (l + r) // 2
            cur = 0
            for pile in piles:
                cur += math.ceil(pile / mid)
            if cur <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res


        