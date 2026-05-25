class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        for i in range(len(strs[0])):
            cur = strs[0][i]
            for word in strs:
                if word[i] != cur:
                    return strs[0][:i]
        return strs[0]
        