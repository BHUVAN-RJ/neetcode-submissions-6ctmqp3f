class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        freq = [[] for i in range(len(nums) + 1)]

        for key, val in count.items():
            freq[val].append(key)
        
        res = []
        for vals in reversed(freq):
            while len(res) < k and vals:
                res.append(vals.pop())
        
        return res


        