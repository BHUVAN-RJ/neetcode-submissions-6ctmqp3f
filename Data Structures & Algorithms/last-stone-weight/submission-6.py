'''
we get the

'''

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            stone_one = heapq.heappop_max(stones)
            stone_two = heapq.heappop_max(stones)
            diff = abs(stone_one - stone_two)
            if diff > 0:
                heapq.heappush_max(stones, diff)
        
        if stones:
            return stones[0]
        else:
            return 0
