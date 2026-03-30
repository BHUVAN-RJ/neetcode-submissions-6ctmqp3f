class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ordS = [0] * 26
        ordT = [0] * 26

        for i in s:
            cur = ord(i) - ord('a')
            ordS[cur] += 1
        
        for i in t:
            cur = ord(i) - ord('a')
            ordT[cur] += 1
        
        if ordS == ordT:
            return True
        else:
            return False
        