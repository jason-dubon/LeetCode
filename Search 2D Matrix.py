class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left = 0
        right = len(matrix) - 1
        
        while left <= right:
            mid = (right + left) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] > target:
                right = mid - 1
            if matrix[mid][0] < target:
                l = 0
                r = len(matrix[mid]) - 1
                if matrix[mid][r] < target:
                    left = mid + 1
                    continue
                while l <= r:
                    m = (l + r) // 2
                    if matrix[mid][m] == target:
                        return True
                    elif matrix[mid][m] > target:
                        r = m - 1
                    elif matrix[mid][m] < target:
                        l = m + 1
                return False
        
        return False