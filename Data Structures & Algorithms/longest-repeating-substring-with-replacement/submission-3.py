class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l, r = 0, 0
        res = 0
        while r < len(s):
            windowSize = (r - l) + 1
            freq[s[r]] = 1 + freq.get(s[r], 0)
            maxFreq = max(freq.values())
            r += 1
            if windowSize - maxFreq <= k:
                res = max(windowSize, res)
            else:
                freq[s[l]] -= 1
                l += 1
        return res

                




        