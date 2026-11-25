class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        s = s.lower()
        def isalphanum(char):
            if ord('a') <= ord(char) <= ord('z'):
                return True
            elif ord('0') <= ord(char) <= ord('9'):
                return True
            else:
                return False
        
        while l <= r:
            if not isalphanum(s[l]):
                print(s[l])
                l += 1
                continue
            if not isalphanum(s[r]):
                print(s[r])
                r -= 1
                continue
            if s[l] != s[r]:
                print(s[l], s[r])
                return False
            l += 1
            r -= 1
        
        return True
        