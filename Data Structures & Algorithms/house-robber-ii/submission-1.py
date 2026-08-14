'''
another dp problem - but 2 twists

1. each house has a money aspect - this was there in prev
2. the list is a circular list


how to handle the circular list problem - 
list has 3 elements - [1,2,3] - cannot do 1 and 3
list has 5 elemets - [1,2,3,4,5] - combination (1,3)(2,4)(3,5)
[1,2, 4, 6]
[5, 5, 8, 8]

[2, 9, 10, 12]
[6, 6, 14, 15]

exactly like house robber 1 but cannot add the final element
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        dp_left = [nums[0], max(nums[1], nums[0])]

        for i in range(2, len(nums) - 1):
            dp_left.append(max(dp_left[-1], dp_left[-2] + nums[i]))
        
        dp_right = [nums[-1], max(nums[-1], nums[-2])]

        for i in reversed(range(1, len(nums) - 2)):
            dp_right.append(max(dp_right[-1], dp_right[-2] + nums[i]))
        
        return max(dp_left[-1], dp_right[-1])


        