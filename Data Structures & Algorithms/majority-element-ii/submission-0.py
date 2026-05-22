class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        res = []
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > len(nums) // 3 and num not in res:
                res.append(num)
        return res
        