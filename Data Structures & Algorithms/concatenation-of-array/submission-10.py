class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        i = 0
        while length > 0:
            nums.append(nums[i])
            i +=1
            length -=1
        
        return nums