class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i in range(len(nums)):
            reqNum = target - nums[i]
            if reqNum in visited:
                return [min(i, visited[reqNum]), max(i, visited[reqNum])]
            else:
                visited[nums[i]] = i
        