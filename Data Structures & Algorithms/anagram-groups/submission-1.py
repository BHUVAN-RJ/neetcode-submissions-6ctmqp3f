class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        res = []
        
        for word in strs:
            curWord = [0] * 26
            for char in word:
                val = ord(char) - ord('a')
                curWord[val] += 1
            curWord = tuple(curWord)
            if curWord in groups:
                groups[curWord].append(word)
            else:
                groups[curWord] = [word]
        
        for k,v in groups.items():
            res.append(v)
        return res