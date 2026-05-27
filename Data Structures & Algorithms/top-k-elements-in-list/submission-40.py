class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        groups = [[] for i in range(len(nums) + 1)]
        for key,val in count.items():
            groups[val].append(key)
        
        res = []
        for i in range(len(groups) - 1, -1, -1):
            for num in groups[i]:
                res.append(num)
                if len(res) == k:
                    return res
        