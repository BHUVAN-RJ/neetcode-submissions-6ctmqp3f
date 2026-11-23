'''
convert each to [0]* 26 -> create key
{[0]:[vals]} -> convert to list send


'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            
            key = tuple(key)
            groups[key] = groups.get(key, []) + [s]
        
        res = []
        for key, val in groups.items():
            res.append(val)
        
        return res

        