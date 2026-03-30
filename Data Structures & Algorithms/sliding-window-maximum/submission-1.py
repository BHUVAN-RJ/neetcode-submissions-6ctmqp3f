class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        curMax = -float('inf')
        res = []
        l = 0
        for r in range(k):
            curMax = max(curMax, nums[r])
        
    
        while r < len(nums) - 1:
            res.append(curMax)
            l += 1
            r += 1
            if nums[l - 1] == curMax:
                curMax = -float('inf')
                for i in range(l,r):
                    curMax = max(curMax, nums[i])
            curMax = max(nums[r], curMax)
        res.append(curMax)
        return res