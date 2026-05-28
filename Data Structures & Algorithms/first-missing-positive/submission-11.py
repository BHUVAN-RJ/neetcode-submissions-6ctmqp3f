# simpler uses hash set to store the values and give solution - easier

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        curset = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in curset:
                return i
        return len(curset ) + 1

        