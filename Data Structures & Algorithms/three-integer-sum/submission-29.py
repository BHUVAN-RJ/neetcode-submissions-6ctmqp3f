'''
[-1, 0, 1]
[-1, 2, -1]

[-4, -1, -1, 0, 1, 2]
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                cur = nums[l] + nums[r] + nums[i]
                if cur == 0:
                    res.add((nums[l], nums[r], nums[i]))
                    l += 1
                    r -= 1
                elif cur < 0:
                    l += 1
                else:
                    r -= 1
        return list(res)


                
        