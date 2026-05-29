class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1, w2 = 0, 0
        res = ''
        cur = 0
        while w1 < len(word1) and w2 < len(word2):
            if len(res) % 2 == 0:
                res += word1[w1]
                w1 += 1
            else:
                res += word2[w2]
                w2 += 1
        
        while w1 < len(word1):
            res += word1[w1]
            w1 += 1
        
        while w2 < len(word2):
            res += word2[w2]
            w2 += 1
        return res
        