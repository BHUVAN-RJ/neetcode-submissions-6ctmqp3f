class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}

        for i in range(len(nums)):
            curdiff = target - nums[i]
            if curdiff in diff:
                return [diff[curdiff], i]
            else:
                diff[nums[i]] = i
            
        