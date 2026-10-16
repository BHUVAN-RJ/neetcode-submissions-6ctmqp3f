class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        visitSet = set()
        res = []
        completed = set()

        for crs, pre in prerequisites:
            preMap[crs].append(pre)


        def dfs(crs):
            if crs in visitSet:
                return False
            
            if crs in completed:
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            
            visitSet.remove(crs)
            preMap[crs] = []
            completed.add(crs)
            res.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []
        
        return res

        