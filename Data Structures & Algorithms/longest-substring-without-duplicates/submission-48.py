class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l,r = 0, 0
        subs = set()
        res = 1
        while r < len(s):
            if s[r] in subs:
                res = max(res, len(subs))
                while s[r] in subs:
                    subs.remove(s[l])
                    l += 1
            subs.add(s[r])
            r += 1
        res = max(res, len(subs))
        return res
        