class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                left1 = 0
                right1 = len(matrix[mid]) - 1
                while left1 < right1:
                    mid1 = (left1 + right1) // 2
                    if target == matrix[mid][mid1]:
                        return True
                    if target < matrix[mid][mid1]:
                        right1 = mid1-1
                    if target > matrix[mid][mid1]:
                        left1 = mid1 + 1

                if left1 == right1 and target == matrix[mid][left1]:
                    return True
                return False
            if target < matrix[mid][0]:
                right = mid-1
            if target > matrix[mid][-1]:
                left = mid + 1
        return False