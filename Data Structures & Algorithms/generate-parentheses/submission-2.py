class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        tmp = []
        def backtrack(openC, closedC):
            if openC == closedC == n:
                res.append("".join(tmp))
                return
            
            if openC < n:
                tmp.append('(')
                backtrack(openC + 1, closedC)
                tmp.pop()
            
            if closedC < openC:
                tmp.append(')')
                backtrack(openC, closedC + 1)
                tmp.pop()
        
        backtrack(0, 0)
        return res
            
        

        