class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = rows-1
        mid = 0
        while l <= r:
            mid = l + (r-l)//2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                break
            elif target > matrix[mid][-1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
        row = matrix[mid]
        l = 0
        r = len(matrix[mid])-1
        while l <= r:
            mid = l + (r-l)//2
            if target == row[mid]:
                return True
            if target > row[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return False
        