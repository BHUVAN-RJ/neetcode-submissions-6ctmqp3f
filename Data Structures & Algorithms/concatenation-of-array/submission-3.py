class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            res.insert(i, nums[i])
            res.append(nums[i])
        return res

        