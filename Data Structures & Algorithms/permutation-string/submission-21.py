class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        word1 = [0] * 26
        word2 = [0] * 26

        for i in range(len(s1)):
            word1[ord(s1[i]) - ord('a')] += 1
            word2[ord(s2[i]) - ord('a')] += 1
        
        l, r = 0, len(s1)
        while r < len(s2):
            print(s2[l:r+1])
            if word1 == word2:
                return True
            
            word2[ord(s2[r]) - ord('a')] += 1
            word2[ord(s2[l]) - ord('a')] -= 1
            r += 1
            l += 1
        return word1 == word2


        


        