class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        visited = {}
        i = 0
        while i < len(nums):
            if nums[i] in visited:
                nums.pop(i)
            else:
                visited[nums[i]] = 1
                i += 1
        return len(nums)