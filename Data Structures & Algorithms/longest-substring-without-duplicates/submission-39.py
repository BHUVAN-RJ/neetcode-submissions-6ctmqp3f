class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        substring = {}
        while r < len(s):
            if s[r] in substring:
                l = max(substring[s[r]] + 1, l)
            substring[s[r]] = r
            res = max(res, (r-l + 1))
            r += 1
        
        return res

        