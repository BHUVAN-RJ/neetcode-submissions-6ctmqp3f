class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = 0
        r = len(s) - 1
        while l < r:
            if not self.isAlphaNum(s[l]):
                l += 1
                continue
            elif not self.isAlphaNum(s[r]):
                r -= 1
                continue
            elif s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

            

    def isAlphaNum(self, char):
        if ord(char) >= ord('0') and ord(char) <= ord('9'):
            return True
        elif ord(char) >= ord('a') and ord(char) <= ord('z'):
            return True
        return False
        