# might be similar to coco eating banana
# but how can we get the max  - like 8 in the example 3
# max = 500 -> max weights[i] -> ok for now
# l = 1, r = 500 - m = 250
# [1,5,4,4,2,3] -> 1 day -> valid -> r = 250 - 1, res = 500
# l = 1, r = 249 - m = 125
# [1,5,4,4,2,3] -> 1 day -> valid -> r = 125 - 1, res = 250
# l = 1, r = 124 - m = 75
# [1,5,4,4,2,3] -> 1 day -> valid -> r = 75 - 1, res = 150
# l = 1, r = 74 - m = 
# [1,5,4,4,2,3] -> 1 day -> valid -> r = 75 - 1, res = 150
# we can clearly see max/r is too much -> thesis the max weight per day can be:
# when all items are same -> [5,5,5,5,5,5] and dayys = 3 -> max/r can be days * max(arr) -> 5*3
# l = 1, r = 15, m = 8 
# [1,2,3,4,5] - days = 4
# internal loop: thesis - keep adding till val and then next
# 1+2+3, 4, 5 -> 3 --> valid 
# l = 1, r = 7 , m = 4
# 1 + 2, 3, 4, 5 -> 4 -> valid
# 

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        res = max(weights)
        l, r = max(weights), sum(weights)
        # [1,2,3,4,5]
        while l <= r:#l = 1, r = 15, 7, 3, 
            mid = (l+r) // 2 # 4
            curDays = 1 
            curWeight = 0 
            for weight in weights:
                if curWeight + weight <= mid:
                    curWeight += weight #[1+2, 3, 4,]
                else:
                    curDays += 1 # 3
                    curWeight = weight #
            if curDays <= days: # 4 < 5
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res


        