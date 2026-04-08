class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string1 = {}
        string2 = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            string1[s[i]] = string1.get(s[i], 0) + 1
            string2[t[i]] = string2.get(t[i], 0) + 1
        
        for k,v in string1.items():
            if k not in string2:
                return False
            
            if string1[k] != string2[k]:
                return False
        return True
            
        