class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in numSet:
                cur = num
                curLen = 1
                while True:
                    if cur + 1 in numSet:
                        curLen += 1
                        cur += 1
                    else:
                        break
                longest = max(longest, curLen)

        return longest
        