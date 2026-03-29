import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for subMatrix in matrix:
            index = bisect.bisect_left(subMatrix, target) # should return index
            if index < len(subMatrix) and subMatrix[index] == target:
                return True
        return False