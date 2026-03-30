class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # we know that we can maximise the water by maximizing the smaller height thats it
        l = 0
        r = len(heights) - 1
        res = 0
        while l < r:
            curWater = min(heights[l], heights[r]) * (r - l)
            res = max(res, curWater)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res
        