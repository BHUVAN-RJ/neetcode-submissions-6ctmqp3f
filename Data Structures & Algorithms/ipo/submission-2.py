class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxHeap = []
        for i in range(len(profits)):
            maxHeap.append((-profits[i], capital[i]))
        
        heapq.heapify(maxHeap)

        temp = []
        while k > 0:
            temp = []
            cur = None

            while maxHeap and cur == None:
                cur = heapq.heappop(maxHeap)
                if cur[1] <= w:
                    break
                else:
                    temp.append(cur)
                    cur = None
            if not cur:
                return w
            while temp:
                heapq.heappush(maxHeap, temp.pop())
            
            k -= 1
            w += cur[0] * -1
        
        return w


        
        