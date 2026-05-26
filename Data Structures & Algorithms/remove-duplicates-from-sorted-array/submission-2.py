class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        r = 1
        while r < len(nums):
            if nums[r] == nums[r-1]:
                nums.pop(r)
                continue
            r += 1
        return len(nums)



        