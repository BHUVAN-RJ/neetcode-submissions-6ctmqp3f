class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = float('inf')
        while l <= r:
            mid = (l+r) // 2
            print(mid)
            time = 0
            for i in piles:
                time += math.ceil(i/mid)
            
            if time <= h:
                if mid < res:
                    res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
            


        