class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        cols = len(matrix[0])
        r = len(matrix) * cols - 1

        while l <= r:
            m = (l + r) // 2
            row = m // cols
            col = m % cols
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = m + 1
            else:
                r = m - 1
        return False

        