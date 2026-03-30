class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        allowed = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] not in allowed:
                l += 1
                continue
            if s[r] not in allowed:
                r -= 1
                continue
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True