'''
IN: give nums - contains n + 1 integers - each integer is in the range [1,n] inclusive
OUT: return the repeated number
Goal: one number repeats return that particular one only
simple:
we store the elementts one at a time and once the count goes higher we can just return it
O(n) | O(n)


PART 2:
without modifying the array and no extra space
1,2,3,4,5

3 ->

[1,2,-3,2,2]

if I have seen 1 - make 0 +v2
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            print(nums)
            if nums[abs(nums[i]) - 1] < 0:
                return abs(nums[i])
            else:
                nums[abs(nums[i]) - 1] *= -1