class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in index:
                return [min(i, index[needed]), max(i, index[needed])]
            else:
                index[nums[i]] = i
        
        