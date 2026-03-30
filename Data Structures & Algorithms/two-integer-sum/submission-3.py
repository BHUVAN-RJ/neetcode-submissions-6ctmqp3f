class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i in range(len(nums)):
            if nums[i] in visited:
                return [visited[nums[i]], i]
            visited[target - nums[i]] = i
        
        