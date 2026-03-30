class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            curKey = [0] * 26
            for char in word:
                curOrd = ord(char) - ord('a')
                curKey[curOrd] += 1
            curKey = tuple(curKey)
            if curKey in groups:
                groups[curKey].append(word)
            else:
                groups[curKey] = [word]
        
        return list(groups.values())
