class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        def swap(l, r):
            tmp = s[l]
            s[l] = s[r]
            s[r] = tmp
    
        while l < r:
            swap(l, r)
            l += 1
            r -= 1

        