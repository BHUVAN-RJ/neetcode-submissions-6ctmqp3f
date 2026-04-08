class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for word in strs:
            key = [0] * 26
            for char in word:
                val = ord(char) - ord('a')
                key[val] += 1
            key = tuple(key)
            if key not in group:
                group[key] = [word]
            else:
                group[key].append(word)

        
        res = []
        for k, v in group.items():
            res.append(v)
        return res
        
        
        