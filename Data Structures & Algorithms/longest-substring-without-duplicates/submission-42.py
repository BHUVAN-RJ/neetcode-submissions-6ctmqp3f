'''
 zxyzxyz
  l r

res = max(res, r - l + 1) | 1, 2, 3, 3, 3, 3,
{x:4, y:5,z:6 }

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        window = {}
        l, r = 0 , 0
        while r < len(s):
            while s[r] in window:
                del window[s[l]]
                l += 1
            
            window[s[r]] = r

            res = max(res, r - l + 1)
            r += 1
        return res

        