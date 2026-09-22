class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        cur = 0
        res = None
        while cur < k:
            res = heapq.heappop(nums)
            cur += 1
        
        return res * -1

        