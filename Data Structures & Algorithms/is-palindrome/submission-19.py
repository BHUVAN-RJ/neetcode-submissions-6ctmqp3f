class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            if not self.isValid(s[l]):
                l += 1
                continue
            if not self.isValid(s[r]):
                r -= 1
                continue
            
            if s[l] != s[r]:
                print(s[l], s[r], l ,r)
                return False

            l += 1
            r -= 1
        return True



    def isValid(self, c):
        if ord('a') <= ord(c) <= ord('z'):
            return True
        elif ord('0') <= ord(c) <= ord('9'):
            return True
        return False
        