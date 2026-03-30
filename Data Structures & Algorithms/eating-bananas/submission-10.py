class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # [1,4,3,2] -> find k -> max rate at which the person can eat banana 
        # constraint is that you can only complete eating one pile at a time
        # it has to be valid - and minimum val
        # min k is max h
        res = max(piles)

        l,r = 1, max(piles)
        while l <= r:
            mid = math.ceil((l + r) / 2)
            print(l,r,mid)
            current_time = 0
            for num in piles:
                current_time += math.ceil(num / mid)
            print("Current",current_time)
            if current_time <= h:
                r = mid - 1
                res = min(res, mid)
                print("res", res)
            else:
                l = mid + 1
        return res

        