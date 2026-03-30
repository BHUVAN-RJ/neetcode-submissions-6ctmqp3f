class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for i in strs:
            res += str(len(i)) + '#' + i
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l = r = 0
        print(s)
        while r < len(s):
            while s[r] != '#':
                r += 1
            print("len is", s[l:r])
            length = int(s[l:r])
            word = s[r+1:r+length+1]
            r = r + length + 1
            l = r
            res.append(word)
        return res 
