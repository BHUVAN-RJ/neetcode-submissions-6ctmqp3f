class Solution:
    def reorganizeString(self, s: str) -> str:
        q = deque()
        count = Counter(s)
        maxHeap = [[-v, k] for k,v in count.items()]
        heapq.heapify(maxHeap)
        print(maxHeap)

        res = ''
        prev = None
        while maxHeap:
            cur = heapq.heappop(maxHeap)
            res += cur[1]
            cur[0] += 1
            if prev and prev[0] < 0:
                heapq.heappush(maxHeap, prev)
            prev = cur
        if prev[0] < 0:
            return ""
        return res
            

        
        