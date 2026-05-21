class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        arr = [[] for i in range(len(nums) + 1)]
        print(arr)
        for key, val in count.items():
            arr[val].append(key)
        
        
        res = []
        
        for i in range(len(arr) - 1, -1, -1):
            print(res)
            for num in arr[i]:
                if len(res) == k:
                    return res
                res.append(num)
            if len(res) == k:
                return res

        