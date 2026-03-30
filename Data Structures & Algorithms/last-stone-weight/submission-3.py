class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we have two stones heaviest -> heap -> and then we just keep mashing and joining until one is left
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones, first - second)
        
        if len(stones) == 0: return 0
        else: return abs(stones[0])

        