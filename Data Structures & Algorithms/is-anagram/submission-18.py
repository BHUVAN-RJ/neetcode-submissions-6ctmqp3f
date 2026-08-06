class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        one, two = [0] * 26, [0] * 26
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            one[ord(s[i]) - ord('a')] += 1
            two[ord(t[i]) - ord('a')] += 1
        return one == two
        