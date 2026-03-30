class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                res += max(maxL - height[l], 0)
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += max(maxR - height[r], 0)
        return res
        