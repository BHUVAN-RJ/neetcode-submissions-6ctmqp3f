class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        groups = [[] for i in range(len(nums) + 1)]
        for key, val in count.items():
            groups[val].append(key)
        
        res = []
        for i in range(len(nums), -1, -1):
            for n in groups[i]:
                res.append(n)
                if len(res) == k:
                    return res
        