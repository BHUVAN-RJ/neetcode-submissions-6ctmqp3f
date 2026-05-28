class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

            if len(count) <= 2:
                continue
            
            newcount = defaultdict(int)
            for k,v in count.items():
                if v > 1:
                    newcount[k] = v - 1
            
            count = newcount

        res = []
        for k in count:
            if nums.count(k) > len(nums) // 3:
                res.append(k)
        return res
        