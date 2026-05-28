class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixSum = {0:1}
        cursum = 0
        for num in nums:  #2
            cursum += num   #2-1+1+2 = 3
            res += prefixSum.get(cursum - k, 0)
            prefixSum[cursum] = prefixSum.get(cursum, 0) + 1 # {0:1, 2:2, 1:1}
        
        return res