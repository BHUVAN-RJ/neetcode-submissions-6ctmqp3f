# goal -> split the array into k sub arrays(continious)

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        r = sum(nums)
        l = max(nums)
        res = r
        while l <= r:
            mid = (l+r) // 2
            # check if its possible to make suck groups
            groups = 0
            cursum = 0
            for num in nums:
                cursum += num
                if cursum > mid:
                    groups += 1
                    cursum = num
            groups += 1
            if groups <= k:
                res = mid
                r = mid - 1
                
            else:
                l = mid + 1
        return res

            
