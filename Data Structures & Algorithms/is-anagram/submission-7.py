class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string1 = [char for char in s]
        for char in t:
            if char in string1:
                string1.remove(char)
            else:
                return False
        if len(string1) == 0:
            return True
        else:
            return False
            
        