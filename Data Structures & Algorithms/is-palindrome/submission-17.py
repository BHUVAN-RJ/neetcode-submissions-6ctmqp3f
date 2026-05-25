class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        s = s.lower()
        print(s)
        while l < r:
            if not self.isValid(s[l]):
                l += 1
                continue
            if not self.isValid(s[r]):
                r -= 1
                continue
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True



    def isValid(self, c):
        if ord('a') <= ord(c) and ord(c) <= ord('z'):
            return True
        if ord('0') <= ord(c) and ord(c) <= ord('9'):

            return True
        return False
        