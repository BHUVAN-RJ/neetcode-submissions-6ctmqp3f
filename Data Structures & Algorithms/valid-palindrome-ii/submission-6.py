class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1  
            else:
                left = s[l:r]
                right = s[l+1:r+1]
                # print(s[l:r], s[r-1:l-1:-1], s[l+1:r+1], s[r:l:-1])
                if s[l:r] == s[r-1:l-1:-1] or s[l+1:r+1] == s[r:l:-1]:
                    return True
                # if left == left[::-1] or right == right[::-1]:
                #     return True
                else:
                    return False
        return True
        