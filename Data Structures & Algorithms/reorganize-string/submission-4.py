class Solution:
    def reorganizeString(self, s: str) -> str:
        #get the freq every time -> min heapify it and then use the number that has max freq 
        freq = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in freq.items()]
        res = ''
        prev = None
        while len(res) < len(s):
            heapq.heapify(maxHeap)
            print(maxHeap)
            idx = 0
            if prev == maxHeap[0][1]:
                if len(maxHeap) > 1:
                    idx = 1
                else:
                    return ''
            
            res += maxHeap[idx][1]
            maxHeap[idx][0] += 1
            prev = maxHeap[idx][1]
            if maxHeap[idx][0] == 0:
                maxHeap.pop(idx)
        return res



        
            
        