class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def oneRotation(iInitial, jInitial, maxI, minI, maxJ, minJ):
            i = iInitial
            j = jInitial+1
            prevI = i
            prevJ = j-1
            replaced = matrix[i][j]
            matrix[i][j] = matrix[prevI][prevJ]
            while i != iInitial or j != jInitial:
                if i == minI:
                    if j + 1 <= maxJ:
                        j += 1
                    else:
                        i += 1
                    save = matrix[i][j]
                    matrix[i][j] = replaced
                    replaced = save
                elif j == maxJ:
                    if i + 1 <= maxI:
                        i += 1
                    else:
                        j -= 1
                    save = matrix[i][j]
                    matrix[i][j] = replaced
                    replaced = save
                elif i == maxI:
                    if j - 1 >= minJ:
                        j -= 1
                    else:
                        i -= 1
                    save = matrix[i][j]
                    matrix[i][j] = replaced
                    replaced = save
                elif j == minJ:
                    if i - 1 >= minI:
                        i -= 1
                    else:
                        j += 1
                    save = matrix[i][j]
                    matrix[i][j] = replaced
                    replaced = save
        n = len(matrix)
        i = 0
        j = 0
        for _ in range(n//2):
            for _ in range(n-2*i-1):
                oneRotation(i, j, n-i-1, i, n-j-1, j)
            i += 1
            j += 1
        


        