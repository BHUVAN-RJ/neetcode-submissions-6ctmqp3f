class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        idx = 0
        res = ''
        sorted(strs, key=lambda x:len(x))
        
        if '' in strs:
            return ''
        while True:
            if idx < len(strs[0]):
                char = strs[0][idx]
            else:
                return res
            for word in strs:
                if idx >= len(word):
                    return res
                elif word[idx] != char:
                    return res
            idx += 1
            res += char
        return res



        