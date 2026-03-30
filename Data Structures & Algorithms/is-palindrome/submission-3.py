class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if not self.isValid(s[l]):
                l += 1
                continue
            if not self.isValid(s[r]):
                r -= 1
                continue
            
            if s[l].lower() != s[r].lower():
                print(s[l], s[r])
                return False
            
            l += 1
            r -= 1
        return True

    def isValid(self, char):
        if ord(char) >= ord("A") and ord(char) <= ord("Z"):
            return True
        if ord(char) >= ord("a") and ord(char) <= ord("z"):
            return True
        if ord(char) >= ord("0") and ord(char) <= ord("9"):
            return True
        return False
        