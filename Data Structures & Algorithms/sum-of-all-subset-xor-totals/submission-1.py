'''


'''

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = []
        cur = []
        def  backtrack(i):
            if i >= len(nums):
                subsets.append(cur.copy())
                return                
            cur.append(nums[i])
            backtrack(i + 1)
            cur.pop()
            backtrack(i + 1)
        
        print(subsets)
        backtrack(0)
        cursum = 0
        for items in subsets:
            cur = 0
            for num in items:
                cur = cur ^ num
            cursum += cur
        
        return cursum




        