class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = [0] * 26
        word2 = [0] * 26

        for c in s:
            cur = ord(c) - ord('a')
            word1[cur] += 1
        
        for c in t:
            cur = ord(c) - ord('a')
            word2[cur] += 1
        
        return word1 == word2
        