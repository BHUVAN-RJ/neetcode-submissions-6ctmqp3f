# basically its one big sorted array but each row is of len m  and there are n rows
# core check if last element is <= target or >
# if greater check for next
# then do a binary search on the cur array thats it   ==> n(log m)
# so for log(m*n) -> 
# we need to do a binary search on the entire thing.
# l = 0,0 r = m, n



class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = (len(matrix) * len(matrix[0])) - 1
        while l <= r:
            m = (l+r) // 2
            if matrix[m // len(matrix[0])][m % len(matrix[0])] == target:
                return True
            elif  matrix[m // len(matrix[0])][m % len(matrix[0])] < target:
                l = m + 1
            else:
                r = m - 1
        return False 
        