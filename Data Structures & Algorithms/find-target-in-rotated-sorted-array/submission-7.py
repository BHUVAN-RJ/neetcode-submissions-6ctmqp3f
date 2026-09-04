'''
cases for l and r:
    l <= m <= r:
        means normal sorted array and m is in the right sorted part then we can do the actual binary search in this part
    l <= m >= r:
        means m is in the left sorted array part and we need to move l = m + 1
    if  m == target: return


'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[l] <= nums[m] <= nums[r]:
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            elif nums[l] >= nums[m] <= nums[r]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1 
            else:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

                
        return -1        