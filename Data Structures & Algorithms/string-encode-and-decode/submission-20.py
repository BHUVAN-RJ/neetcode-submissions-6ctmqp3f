class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            res += str(len(word)) + '#' + word
        
        return res


    def decode(self, s: str) -> List[str]:
        l, r = 0, 0
        res = []
        while r < len(s):
            while s[r] != '#':
                r += 1
            length = int(s[l:r])
            r += 1
            res.append(s[r:r+length])
            r += length
            l = r
        return res

