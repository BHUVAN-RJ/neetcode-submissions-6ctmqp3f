class Solution:
    def minWindow(self, s: str, t: str) -> str:
        neededCount = {}
        for c in t:
            neededCount[c] = neededCount.get(c, 0) + 1
        
        window = {}
        l, r = 0, 0
        haveCount = 0
        res = ''
        while r < len(s):
            
            if s[r] in neededCount:
                window[s[r]] = window.get(s[r], 0) + 1
                if window[s[r]] == neededCount[s[r]]:
                    haveCount += 1
                print(window)
                
                if haveCount == len(neededCount):
                    print("match")
                    while haveCount == len(neededCount):
                        if s[l] in window:
                            window[s[l]] -= 1
                            if window[s[l]] < neededCount[s[l]]:
                                haveCount -= 1
                        l += 1
                    if res == '':
                        res = s[l-1:r+1]
                    else:
                        cur = s[l-1:r+1]
                        res = s[l-1:r+1] if len(cur) <= len(res) else res
                    print(res, l-1, r)
            r += 1
        return res
                

           
        

        