class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        longest = 1
        substring = {s[0]:0}
        l, r = 0, 1
        while r < len(s):
            if s[r] in substring:
                longest = max(longest, (r-l))
                while s[r] in substring:
                    substring.pop(s[l])
                    l += 1
            else:
                substring[s[r]] = r
                r += 1
        longest = max(longest, (r-l))
        return longest