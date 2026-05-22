class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        m = 0
        def swap(l,r):
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
        while m <= right:
            if nums[m] == 0:
                swap(left, m)
                left += 1
                
            elif nums[m] == 2:
                swap(m, right)
                right -= 1
                continue
            m += 1
            

        