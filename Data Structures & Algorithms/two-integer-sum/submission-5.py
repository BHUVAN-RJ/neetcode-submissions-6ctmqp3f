class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in needed:
                return [ needed[diff], i]
            else:
                needed[nums[i]] = i

        