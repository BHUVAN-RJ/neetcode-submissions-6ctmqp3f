class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            cur = [0] * 26
            for char in word:
                place = ord(char) - ord('a')
                cur[place] += 1
            
            cur = tuple(cur)
            if cur not in groups:
                groups[cur] = []    
            groups[cur].append(word)
        
        return list(groups.values())
        