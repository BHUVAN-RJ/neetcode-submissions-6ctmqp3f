class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            key = [0] * 26
            for char in s:
                key[ord(char) - ord('a')] += 1
            
            groups[tuple(key)] = [s] + groups.get(tuple(key), [])
        
        return list(groups.values())

        