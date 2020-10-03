class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 1 and len(matrix[0]) == 0:
            return False
        index = -1
        for i in range(len(matrix)):
            if target <= matrix[i][-1]:
                index = i
                break

        if index == -1:
            return False
        else:
            left, right = 0, len(matrix[0])-1
            while left <= right:
                mid = (left+right) // 2
                if matrix[index][mid] > target:
                    right = mid-1
                elif matrix[index][mid] < target:
                    left = mid+1
                else:
                    return True
            return False