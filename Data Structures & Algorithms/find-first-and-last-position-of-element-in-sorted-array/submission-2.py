class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(leftbias):
            l, r = 0, len(nums) - 1
            i = -1
            while l <= r:
                mid = (l+r) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    i = mid
                    if leftbias:
                        r = mid - 1
                    else:
                        l = mid + 1
            return i
        left = binary_search(True)
        right = binary_search(False)
        return [left, right]
        