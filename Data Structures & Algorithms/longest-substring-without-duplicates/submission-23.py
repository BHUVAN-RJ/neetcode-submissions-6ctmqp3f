class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #abbaceds
        l, r = 0, 0
        res = 0
        substring = {}
        while r < len(s):
            if s[r] in substring:
                length = r - l
                res = max(res, length)
                while s[r] in substring:
                    del substring[s[l]]
                    l += 1
                
            substring[s[r]] = r
            r += 1
        res = max(r-l, res)
        return res


        