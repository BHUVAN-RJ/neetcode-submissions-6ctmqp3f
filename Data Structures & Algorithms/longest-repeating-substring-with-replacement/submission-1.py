class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l, r = 0, 0
        res = 0

        while r < len(s):
            curChar = s[r]
            freq[curChar] = 1 + freq.get(curChar, 0)
            windowSize = (r - l) + 1
            maxFreq = max(freq.values())
            print(freq)
            print(maxFreq)
            r += 1
            if windowSize - maxFreq <= k:
                res = max(windowSize, res)
            else:
                freq[s[l]] -= 1
                l += 1
        return res
                




        