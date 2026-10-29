'''


[2,9,8,3,6]
(0, 2) (2, 9) 
'''



class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        
        for i in range(len(nums)):
            temp = max(nums[i] + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2
        