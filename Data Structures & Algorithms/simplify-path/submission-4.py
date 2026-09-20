'''
question:
1. can the absolute path not start with '/'
2. should I resolve the .. -> have to resolve them 

stack = ['neetcode','practice', 'courses']

/neetcode/practice//...///../courses/
                                    l r

/ -> until I get next non / increment r
. -> until I gget next non . increment

can use stack -> push and pop if ..
/_home/a/


[]
res = "".join(stack, '/')
res = ''
res += '/'
'''



class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        l,r = 0 ,0
        while r < len(path):
            if path[r] == '/': 
                while r < len(path) and path[r] == '/' :
                    r += 1
                l = r
            while r < len(path) and path[r] != '/':
                r += 1
            
            cur = path[l:r]
            if cur == '.':
                continue
            elif cur == '..':
                if stack:
                    stack.pop()
            elif len(cur) > 0:
                stack.append(cur)
            else:
                continue
        
        res = "/".join(stack)
        print(res)
        print(stack)
        res = '/' + res

        return res



                
        