class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(len(nums)):
            cur_idx = abs(nums[i]) - 1
            if cur_idx < 0 or cur_idx >= len(nums):
                continue
            elif nums[cur_idx] == 0:
                nums[cur_idx] = -(len(nums) + 2)
            elif nums[cur_idx] < 0:
                continue
            else:
                nums[cur_idx] = -nums[cur_idx]
        
        for i in range(1, len(nums) + 1):
            print("cn")
            if nums[i-1] < 0:
                continue
            else:
                return i
        
        return len(nums) + 1
            

        