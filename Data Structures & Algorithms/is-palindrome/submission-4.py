class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s) - 1
        while l <= r:
            print(s[l], s[r])
            if not self.isValid(s[l]):
                l += 1
                continue
            if not self.isValid(s[r]):
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def isValid(self, c):
        val = ord(c)
        if val <= ord('Z') and val >= ord('A'):
            return True
        if ord('a') <= val and val <= ord('z'):
            return True
        if ord('0') <= val and val <= ord('9'):
            return True
        return False
        