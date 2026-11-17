class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        for i in range (len(matrix)):
            mat  =matrix[i]
            n = len(mat)-1
            if target <= mat[n]:
                left =0
                right = len(mat) -1
                while left <= right:
                    mid = left + (right- left) //2
                    if target == mat[mid]:
                        return True
                    elif target < mat[mid]:
                        right = mid -1
                    else:
                        left = mid +1
        return False