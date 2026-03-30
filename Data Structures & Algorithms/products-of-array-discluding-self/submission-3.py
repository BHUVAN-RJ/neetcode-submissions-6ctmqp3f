class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        1,1,2,8

        42,24,6,1
        [42, 24, 12, 8]
        res = [1] * len(nums)
        prev = 1
        for i in range(len(nums)):
            res[i] *= prev
            prev *= nums[i]
        
        prev = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= prev
            prev *= nums[i]

        return res