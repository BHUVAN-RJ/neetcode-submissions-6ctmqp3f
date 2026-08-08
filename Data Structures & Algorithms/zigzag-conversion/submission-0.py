
'''
G   I   N
O E S I G
O L H R
G   I


I should start putthing it rowwise
for the seconf loop - total - 2 - ALSO REVERSE
TOP DOWN - BOTTOM UP
[[GIN]
[OESIG]
[OLHR]
[GI]]
'''


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        resMatrix = [[] for i in range(numRows)]
        cur = 0
        topdown = True
        while cur < len(s):
            if topdown:
                #the normal loop
                count = 0
                while count < numRows and cur < len(s):
                    resMatrix[count].append(s[cur])
                    count += 1
                    cur += 1
                topdown = False

            else:
                # the other loop
                count = numRows - 2
                while count > 0 and cur < len(s):
                    resMatrix[count].append(s[cur])
                    count -= 1
                    cur += 1
                topdown = True
        
        print(resMatrix)
        res = []
        for row in resMatrix:
            res.append(''.join(row))
        
        return ''.join(res)



        