class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            
            rem_left = s[l+1:r+1]
            rem_right = s[l:r]
            print(rem_left)

            return (rem_left == rem_left[::-1] or rem_right == rem_right[::-1])
        return True
                    

        