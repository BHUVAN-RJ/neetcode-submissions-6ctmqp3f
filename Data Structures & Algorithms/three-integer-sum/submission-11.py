class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for l in range(len(nums) - 2):
            if l > 0 and nums[l] == nums[l-1]:
                continue
            p1 = l + 1
            p2 = len(nums) - 1
            while p1 < p2:
                curSum = nums[l] + nums[p1] + nums[p2]
                if curSum == 0:
                    res.append([nums[l], nums[p1], nums[p2]])
                    p1 += 1
                    while p1 < p2 and nums[p1] == nums[p1-1]:
                        p1 +=1
                elif curSum < 0:
                    p1 += 1
                else:
                    p2 -= 1
            
        return res
            
            
        