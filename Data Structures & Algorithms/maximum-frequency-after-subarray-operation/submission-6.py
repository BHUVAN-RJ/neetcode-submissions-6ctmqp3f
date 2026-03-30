class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        res = 0
        freq = {}
        for num in nums:
            freq[num] = max(freq.get(num, 0), freq.get(k, 0)) + 1
            res = max(res, freq[num] - freq.get(k,0))
        return res + freq.get(k, 0)
        