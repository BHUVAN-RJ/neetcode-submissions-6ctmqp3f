class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed = {}

        for i in range(len(nums)):
            diff = target - nums[i] 
            if nums[i] in needed:
                return [needed[nums[i]], i]
            
            needed[diff] = i
        