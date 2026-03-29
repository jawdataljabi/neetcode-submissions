class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left <= right:
            middle = (right + left) // 2
            if matrix[middle][0] <= target <= matrix[middle][-1]:
                inLeft = 0
                inRight = len(matrix[middle])
                while inLeft < inRight:
                    inMiddle = (inRight + inLeft) // 2
                    if matrix[middle][inMiddle] >= target:
                        inRight = inMiddle
                    elif matrix[middle][inMiddle] < target:
                        inLeft = inMiddle + 1 # will keep incrementing till left = right
                return True if inLeft < len(matrix[middle]) and matrix[middle][inLeft] == target else False
            elif matrix[middle][0] > target:
                right = middle - 1
            else:
                left = middle + 1

        return False
        