class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = [0] * 26
        word2 = [0] * 26
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            ord1 = ord(s[i]) - ord('a')
            ord2 = ord(t[i]) - ord('a')
            word1[ord1] += 1
            word2[ord2] += 1
        return word1 == word2