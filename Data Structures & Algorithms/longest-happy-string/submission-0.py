'''
aaaaaa, bb
aabaabaa

'''
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        if a > 0: maxHeap.append([-a, 'a'])
        if b > 0: maxHeap.append([-b, 'b'])
        if c > 0: maxHeap.append([-c, 'c'])
        
        heapq.heapify(maxHeap)
        res = ''

        while maxHeap:
            print(res, maxHeap)
            cur = heapq.heappop(maxHeap)
            if len(res) >= 2:
                if res[-1] == res[-2] == cur[1]:
                    if not maxHeap:
                        return res
                    temp = heapq.heappop(maxHeap)
                    res += temp[1]
                    temp[0] += 1
                    if temp[0] != 0:
                        heapq.heappush(maxHeap, temp)
                    if cur[0] != 0:
                        heapq.heappush(maxHeap, cur)
                else:
                    res += cur[1]
                    cur[0] += 1
                    if cur[0] != 0:
                        heapq.heappush(maxHeap, cur)
            else:
                res += cur[1]
                cur[0] += 1
                if cur[0] != 0:
                    heapq.heappush(maxHeap, cur)
        return res


        