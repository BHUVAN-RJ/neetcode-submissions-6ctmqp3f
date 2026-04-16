class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            cur = [0] * 26
            for char in s:
                value = ord(char) - ord('a')
                cur[value] += 1
            key = tuple(cur)
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]
        
        res = []

        for k,v in groups.items():
            res.append(v)
        return res
        