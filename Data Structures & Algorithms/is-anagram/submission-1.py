class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        key1 = [0] * 26
        key2 = [0] * 26

        for i in range(len(s)):
            ord1 = ord(s[i]) - ord('a')
            key1[ord1] += 1
        for i in range(len(t)):
            ord2 = ord(t[i]) - ord('a')
            key2[ord2] += 1

        if tuple(key1) == tuple(key2):
            return True
        else:
            return False