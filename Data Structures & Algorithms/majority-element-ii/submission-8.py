class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i,0) + 1
        
        res = []
        for key,val in count.items():
            if val > len(nums) // 3:
                res.append(key)
        return res