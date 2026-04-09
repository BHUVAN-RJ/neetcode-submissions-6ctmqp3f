class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        
        temp = [[] for i in range(len(nums) + 1)]

        for key,value in count.items():
            temp[value].append(key)
        
        res = []
        for i in range(len(nums), -1, -1):

            while len(res) < k and len(temp[i]) > 0:
                res.append(temp[i].pop())
                if len(res) == k:
                    return res
        