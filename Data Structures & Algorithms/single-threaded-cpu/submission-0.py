'''
[[5,2, 0],[4,4, 1],[4,1, 2],[2,1, 3],[3,3, 4]]

[[2,1,3] - done, [3,3, 4] - done, [4,4, 1],[4,1, 2], [5,2, 0]]

end = 6 - 

'''


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        end = 1
        res = []
        tasks = [tasks[i] + [i] for i in range(len(tasks))]
        tasks.sort(key=lambda x:x[0])
        heap = []
        i = 0
        while i < len(tasks) or heap:

            if not heap and end < tasks[i][0]:
                end = tasks[i][0]
            

            while i < len(tasks) and tasks[i][0] <= end:
                heapq.heappush(heap, [tasks[i][1], tasks[i][2]])
                i += 1
                
            
            cur = heapq.heappop(heap)
            end += cur[0]
            res.append(cur[1])
        
        return res

            

            
            



        