# similar to last question but bit more complex
# [3,5,6,7,8,0,1,2,3,4], target = 2
# l = 0, r = 5 ,m = 2
# 1. if l <= m -> to get to know if m is in left side or right side
#       2. then we do a binary search in that side -> that is just continue
# [5,1,3]
# l = 0, r = 2, m = 1
#  l < m -> false -> 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
        