class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string1 = [0]*26
        string2 = [0]*26
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            ordS = ord(s[i]) - ord('a')
            ordT = ord(t[i]) - ord('a')
            string1[ordS] += 1
            string2[ordT] += 1
        
        for i in range(26):
            if string1[i] != string2[i]:
                return False
        return True

            
        