class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed_difference = {}
        for i in range(len(nums)): #1
            diff = target - nums[i] #3
            if nums[i] in needed_difference:
                return [needed_difference[nums[i]], i]#[0,1]
            else:
                needed_difference[diff] = i#{4:0}
            
        