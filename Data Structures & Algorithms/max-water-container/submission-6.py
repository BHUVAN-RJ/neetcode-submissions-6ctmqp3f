class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        left, right = 0, len(heights) - 1
        while left < right:
            curArea = min(heights[right], heights[left]) * (right - left)
            res = max(res, curArea)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return res


            
        