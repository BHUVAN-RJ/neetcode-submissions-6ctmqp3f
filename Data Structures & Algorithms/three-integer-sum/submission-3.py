class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                
                continue
            print(i)
            l, r = i + 1, len(nums) - 1 
            while l < r:
                curSum = nums[i] + nums[l] + nums[r]
                if curSum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif curSum < 0:
                    l += 1
                else:
                    r -= 1
        return res
            
        

            