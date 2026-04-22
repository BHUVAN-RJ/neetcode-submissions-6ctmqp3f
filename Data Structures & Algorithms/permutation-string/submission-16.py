class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        string1 = {}
        window = {}
        if len(s2) < len(s1):
            return False

        for i in range(len(s1)):
            string1[s1[i]] = string1.get(s1[i], 0) + 1
            window[s2[i]] = window.get(s2[i], 0) + 1


        l = 0
        r = l + len(s1) - 1




        while r + 1 < len(s2):
            if string1 == window:
                return True
            
            r += 1
            window[s2[r]] = window.get(s2[r], 0) + 1
            
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                window.pop(s2[l])
            l += 1
        if string1 == window:
                return True
        return False

            

        