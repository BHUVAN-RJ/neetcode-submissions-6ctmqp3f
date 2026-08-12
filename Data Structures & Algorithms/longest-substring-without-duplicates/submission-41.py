'''
window = []
max = 0
zxyzxyz
  l  r
1, 4
4-2 = 3
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s:
            res = 1
        else:
            res = 0
        l,r = 0,0
        window = set()
        while r < len(s):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            res = max(res, r - l + 1)
            r += 1
        
        return res




        