class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0
        while l <= r:
            cur = (l+r) // 2
            if cur*cur == x:
                return cur
            elif cur*cur > x:
                r = cur - 1
            else:
                res = cur
                l = cur + 1
        return res