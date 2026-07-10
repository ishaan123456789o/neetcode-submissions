class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        seen = set()
        res = []
        curr = (0, 0)
        direction = "right"
        maxI = len(matrix)-1
        maxJ = len(matrix[0])-1
        while True:
            i = curr[0]
            j = curr[1]
            if curr not in seen:
                res.append(matrix[i][j])
            seen.add(curr)
            if (j+1 > maxJ or (i, j+1) in seen) and (i+1 > maxI or (i+1, j) in seen) and (j-1 < 0 or (i, j-1) in seen) and (i-1 < 0 or (i-1, j) in seen):
                break
            if direction == "right":
                if j + 1 <= maxJ and (i, j+1) not in seen:
                    curr = (i, j+1)
                else:
                    direction = "down"
            elif direction == "down":
                if i + 1 <= maxI and (i+1, j) not in seen:
                    curr = (i+1, j)
                else:
                    direction = "left"
            elif direction == "left":
                if j - 1 >= 0 and (i, j-1) not in seen:
                    curr = (i, j-1)
                else:
                    direction = "up"
            elif direction == "up":
                if i - 1 >= 0 and (i-1, j) not in seen:
                    curr = (i-1, j)
                else:
                    direction = "right"
        
        return res


        