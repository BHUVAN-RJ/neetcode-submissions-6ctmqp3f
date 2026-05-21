class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        j = 0
        for i in range(len(strs[0])):
            cur = strs[0][j]
            for word in strs:
                if cur != word[j]:
                    return strs[0][:j]
            j += 1
        return strs[0]