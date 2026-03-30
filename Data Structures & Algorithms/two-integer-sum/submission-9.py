class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i in range(len(nums)):
            if nums[i] in diff:
                return [diff[nums[i]], i]
            cur_diff = target - nums[i]
            diff[cur_diff] = i

