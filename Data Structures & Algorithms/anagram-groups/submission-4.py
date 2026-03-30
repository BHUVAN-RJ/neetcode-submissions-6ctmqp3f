class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            cur = [0] * 26
            for char in word:
                idx = ord(char) - ord('a')
                cur[idx] += 1
            cur = tuple(cur)
            if cur in groups:
                groups[cur].append(word)
            else:
                groups[cur] = [word]
        return list(groups.values())
        