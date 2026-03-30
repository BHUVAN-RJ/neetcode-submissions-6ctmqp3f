class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in nums:
            count[i] = 1 + count.get(i, 0)
        
        freq = [[] for i in range(len(nums) + 1)]
        print(freq)
        for key, value in count.items():
            freq[value].append(key)

        res = []

        for i in range(len(freq) - 1, -1, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
               