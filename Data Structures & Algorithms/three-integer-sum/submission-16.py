class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #while moving skip the same
        # [-4,-1,-1,0,1,2]
        res = []
        nums.sort()
        l = 0
        while l <= len(nums) - 3:
            r = len(nums) - 1
            mid = l + 1
            while mid < r:
                cursum = nums[l] + nums[r] + nums[mid]
                if cursum == 0:
                    res.append([nums[l], nums[r], nums[mid]])
                    mid += 1
                    while mid < r and nums[mid] == nums[mid - 1]:
                        mid += 1
                elif cursum < 0:
                    mid += 1
                else:
                    r -= 1
            l += 1
            while l <= len(nums) - 3 and nums[l] == nums[l-1]:
                l += 1
        return res
                

        