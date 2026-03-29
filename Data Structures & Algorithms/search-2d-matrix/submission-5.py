class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowTop = 0
        rowBottom = len(matrix) - 1

        while rowTop <= rowBottom:
            rowMid = (rowTop + rowBottom) // 2
            if matrix[rowMid][-1] < target:
                rowTop = rowMid + 1
            elif matrix[rowMid][0] > target:
                rowBottom = rowMid - 1
            else:
                break
        
        left = 0
        right = len(matrix[0]) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if matrix[rowMid][mid] == target:
                return True
            elif matrix[rowMid][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False