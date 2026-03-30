class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            curKey = [0] * 26
            for i in word:
                index = ord(i) - ord('a')
                curKey[index] += 1
            key = tuple(curKey)
            if key not in groups:
                groups[key] = [] 
            groups[key].append(word)
            
        
        return list(groups.values())

        