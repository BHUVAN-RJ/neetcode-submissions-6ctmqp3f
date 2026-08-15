'''
find the minimum in an array - 
1. array is rotated n times
2. array is sorted
3. numbers can be -ve

brute force:
minimum

optimal:
logn - binary search

C1
[3,4,5,6,1,2] ==> l = m + 1
l    m     r


[6,7,1,2,3, 4]. ==> r = m - 1
 l     m      r

1 2 3
l m r

NEVER HAPPENIN
 5 4 3 2 1
 l   m   r
 1 5 4 3 2 
 2 1 5 4 3

VAR - min -> 
while l <= r

cases for m:

    m > l but m > r -> m is still in the right section
      l < m > r
    
    m < l but m < r -> m in left section
    l < m < r -> m is in correct section
    l > m > r -> not happen

increasing decreases increasing




DRY RUN:


[2,1]
 lm r
l = 0
r = 1
res = 0
mid = 2
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if len(nums) <= 1:
        #     return min(nums)
        l, r = 0, len(nums) - 1
        res = float('inf') # can be anything in the array

        while l <= r:
            mid = (l+r) // 2
            if nums[mid] < res:
                res = nums[mid]
            
            if nums[l] <= nums[mid] <= nums[r]:
                res = min(res, nums[l])
                break
            elif nums[l] <= nums[mid] and nums[r] <= nums[mid]:
                l = mid + 1
            elif nums[mid] <= nums[l] and nums[mid] <= nums[r]:
                r = mid - 1
        return res
         
















        