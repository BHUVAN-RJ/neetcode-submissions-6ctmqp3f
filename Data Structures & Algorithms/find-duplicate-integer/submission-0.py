class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        prev = -1
        for i in range(len(nums)):
            if prev == nums[i]:
                return nums[i]
            prev = nums[i]
        
            
        