class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        [1, 1, 2, 8]
        [48,24,6,1]
        [48, 24, 12,8]

        res = [1]
        for i  in range(len(nums) - 1):
            res.append(res[-1] * nums[i])
        cur = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= cur
            cur *= nums[i]
        return res
            
        