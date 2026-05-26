class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        word1 = [0] * 26
        word2 = [0] * 26
        if len(s2) < len(s1):
            return False
        for i in range(len(s1)):
            word1[ord(s1[i]) - ord('a')] += 1
            word2[ord(s2[i]) - ord('a')] += 1
        
        r = len(s1)
        l = 0
        if word1 == word2:
            return True
        
        while r < len(s2):
            word2[ord(s2[r]) - ord('a')] += 1
            word2[ord(s2[l]) - ord('a')] -= 1
            if word1 == word2:
                return True
            r += 1
            l += 1
        return False

            
        
        
        

        