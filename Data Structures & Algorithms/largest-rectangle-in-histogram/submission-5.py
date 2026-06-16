class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0 # 7, 7, 
        for i in range(len(heights)): # [7,1,7,2,2,4] STACK:::[(0,1), (1,2), (2, 2)]
            if not stack:
                stack.append((i, heights[i]))
                continue
            
            # can extend
            if heights[i] > stack[-1][1]:
                stack.append((i, heights[i]))
            # cannot extend
            else:
                prevStart = i
                while stack and heights[i] < stack[-1][1]:
                    prevStart = stack[-1][0] # 1
                    area = stack[-1][1] * (i - prevStart) # 7
                    maxArea = max(area, maxArea)
                    stack.pop()
                stack.append((prevStart, heights[i]))
        
        while stack:
            print(stack[-1])
            area = stack[-1][1] * (len(heights) - stack[-1][0])
            maxArea = max(area, maxArea)
            stack.pop()
        
        return maxArea
        