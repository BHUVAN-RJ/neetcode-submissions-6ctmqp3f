class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        key1 = [0] * 26
        key2 = [0] * 26

        for i in range(len(s1)):
            ordA = ord(s1[i]) - ord('a')
            ordB = ord(s2[i]) - ord('a')
            key1[ordA] += 1
            key2[ordB] += 1

        match = 0
        print(match)
        for i in range(len(key1)):
            if key1[i] == key2[i]:
                match += 1

        l = 0
        for r in range(len(s1), len(s2)):
            print(s2[l], s2[r])
            print(match)
            if match == 26:
                return True
            ordL = ord(s2[l]) - ord('a')
            ordR = ord(s2[r]) - ord('a')
            if key2[ordL] == key1[ordL]:
                match -= 1
            key2[ordL] -= 1
            if key2[ordL] == key1[ordL]:
                match += 1
            l += 1
            if key2[ordR] == key1[ordR]:
                match -= 1
            key2[ordR] += 1
            if key2[ordR] == key1[ordR]:
                match += 1
            
        return match == 26

        