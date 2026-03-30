class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0
        r = 0
        while r < len(s):
            while s[r] != '#':
                r += 1
            length = int(s[l:r])
            word = s[r + 1:r+1+length]
            l, r = r+1+length, r+1+length
            res.append(word)
        return res
