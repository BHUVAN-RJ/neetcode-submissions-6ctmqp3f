'''
[4:3]
7-3 = 4
4
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed = {}

        for i in range(len(nums)):
            if nums[i] in needed:
                return [needed[nums[i]], i]
            diff = target - nums[i]
            needed[diff] = i
        

        

        