class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        string1 = [0 for i in range(26)] 
        string2 = [0 for i in range(26)]

        for char in s1:
            string1[ord(char) - ord('a')] += 1
        
        l = 0
        for r in range(len(s2)): # 0, 3 = 3
            if r - l >= len(s1):
                string2[ord(s2[l]) - ord('a')] -= 1
                l += 1
            string2[ord(s2[r]) - ord('a')] += 1
            r += 1
            if string2 == string1:
                return True
        
        return False


        

        


