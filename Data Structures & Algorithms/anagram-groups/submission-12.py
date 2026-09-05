'''

I make groups - key will be the [0,1,1,0] -> ord values thingy
and then we need to make the other 

'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for word in strs:
            cur = [0] * 26
            for s in word:
                index = ord(s) - ord('a')
                cur[index] += 1
            
            cur = tuple(cur)
            if cur in groups:
                groups[cur].append(word)
            else:
                groups[cur] = [word]
        
        res = []
        for k,v in groups.items():
            res.append(v)
        
        return res
        