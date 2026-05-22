class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            curWord = [0] * 26
            for c in word:
                idx = ord(c) - ord('a')
                curWord[idx] += 1
            
            curWord = tuple(curWord)
            if curWord not in groups:
                groups[curWord] = []
            groups[curWord].append(word)
        
        return list(groups.values())
        

        