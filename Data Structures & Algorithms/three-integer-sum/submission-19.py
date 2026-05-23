class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        print(nums)
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                cursum = nums[i] + nums[r] + nums[l]
                if cursum == 0:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif cursum < 0:
                    l += 1
                else:
                    r -= 1
        return list(res)



        