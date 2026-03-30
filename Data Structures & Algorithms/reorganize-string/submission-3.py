class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt, char] for char,cnt in count.items()]
        prev = None
        res = ""
        while len(maxHeap) > 0:
            heapq.heapify(maxHeap)
            cur = 0
            if maxHeap[cur][1] == prev:
                if len(maxHeap) > 1:
                    cur = 1
                else:
                    return ""
            res += f"{maxHeap[cur][1]}"
            prev = maxHeap[cur][1]
            maxHeap[cur][0] += 1
            if maxHeap[cur][0] == 0:
                maxHeap.pop(cur)
                
        return res
        

                
        
        