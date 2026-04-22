class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        string1 = {}
        if len(s2) < len(s1):
            return False

        for i in s1:
            string1[i] = string1.get(i, 0) + 1
        
        window = {}
        l = 0
        r = l + len(s1) - 1
        m = 0
        while m <= r:
            window[s2[m]] = window.get(s2[m], 0) + 1
            m += 1



        while r + 1 < len(s2):
            print(window)
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

            

        