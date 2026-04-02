class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = [[] for i in range(len(nums) + 1)]
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        for key, val in count.items():
            freq[val].append(key)
        
        print(freq)
        for i in range(len(freq) - 1, -1, -1):
            for value in freq[i]:
                if len(res) == k:
                    return res
                res.append(value)


        return res


        
        