class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        res = 0
        for num in nums:
            freq[num] = max(freq[num], freq[k]) + 1
            res = max(res, freq[num] - freq[k])
        return res + freq[k]
