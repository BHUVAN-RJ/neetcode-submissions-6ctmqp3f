class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums) - 1, -1, -1):
            nextDP = dp.copy()
            for element in dp:
                nextDP.add( element + nums[i])
            dp = nextDP

        
        
        if target in dp:
            return True
        else:
            return False

        