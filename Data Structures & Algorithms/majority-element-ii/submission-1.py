class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        res = []
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        for k,v in count.items():
            if v > len(nums) // 3:
                res.append(k)
        
        return res
        