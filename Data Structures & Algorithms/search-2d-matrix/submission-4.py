class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0, len(matrix[0]) - 1
        row = 0
        while l <= r:
            if matrix[row][r] < target:
                row += 1
                if row >= len(matrix):
                    return False
                continue
            
            mid = (l+r) // 2
            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True
        return False
        