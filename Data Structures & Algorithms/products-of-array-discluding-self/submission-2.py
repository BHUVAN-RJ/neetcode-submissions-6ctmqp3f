class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prev = 1
        for i in range(len(nums)):
            res[i] *= prev 
            prev = res[i] * nums[i]
        print(res)
        
        prev = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= prev
            prev *= nums[i]
        return res