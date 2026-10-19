'''



'''

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        res = []

        graphs = {i:[] for i in range(n)}
        for a,b in edges:
            graphs[a].append(b)
            graphs[b].append(a)
        
        print(graphs)


        def dfs(i, cur):
            if graphs[i] == [] and i in visit:
                return 
            cur.append(i)
            visit.add(i)
            for child in graphs[i]:
                if child not in visit:
                    dfs(child, cur)
            
        
        for i in range(n):
            if i in visit:
                continue
            cur = []
            dfs(i, cur)
            if cur:
                res.append(cur)
        
        print(res)
        return len(res)





            

        