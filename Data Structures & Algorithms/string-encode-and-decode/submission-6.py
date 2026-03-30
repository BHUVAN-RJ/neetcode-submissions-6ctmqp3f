class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            res += str(len(word)) + '#' + word
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l, r = 0, 0
        while r < len(s):
            while s[r] != '#':
                r += 1
            length = int(s[l: r])
            word = s[r +1 : r + 1 + length]
            r += length + 1
            l = r
            res.append(word)
        return res
