class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_one = [0] * 26
        word_two = [0] * 26

        for char in s:
            cur = ord(char) - ord('a')
            word_one[cur] += 1
        
        for char in t:
            cur = ord(char) - ord('a')
            word_two[cur] += 1
        
        return word_one == word_two
        