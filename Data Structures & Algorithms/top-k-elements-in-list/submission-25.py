class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        res = []
        for key,val in freq.items():
            print(res)
            res.append((key,val))
            res = sorted(res, key=lambda x:x[1])
            print("sorted ress",res)
            if len(res) > k:
                res.pop(0)
        sorted(res, key=lambda x:x[1])
        print("final_res",res)
        res = [i[0] for i in res]
        return res


        
        