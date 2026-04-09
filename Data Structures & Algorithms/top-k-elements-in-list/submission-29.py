class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        temp = [[] for i in range(len(nums) + 1)]

        for key,value in count.items():
            temp[value].append(key)
        
        res = []
        print(temp, count)
        for i in range(len(nums), -1, -1):

            while len(res) < k and len(temp[i]) > 0:
                    res.append(temp[i].pop())
            if len(res) == k:
                return res
        