class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            key = [0] * 26
            for c in s:
                val = ord(c) - ord('a')
                key[val] += 1
            
            key = tuple(key)
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]
        
        return list(groups.values())
        