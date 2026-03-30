class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        waterTrapped = 0
        l = 0
        r = len(height) - 1
        maxL = 0
        maxR = 0
        while l < r:
            if height[l] <= height[r]:
                water = maxL - height[l]
                if water < 0:
                    maxL = height[l]
                else:
                    waterTrapped += water
                l += 1
            else:
                water = maxR - height[r]
                if water < 0:
                    maxR = height[r]
                else:
                    waterTrapped += water
                r -= 1
        return waterTrapped
                
        