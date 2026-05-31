class Solution:
    def solve(self, board: List[List[str]]) -> None:
        iBoundary = len(board)-1
        jBoundary = len(board[0]) - 1
        seen = set()
        replace = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O" and (i, j) not in seen and i != 0 and i != iBoundary and j != 0 and j != jBoundary:
                    curr = []
                    q = deque()
                    q.append((i, j))
                    curr.append((i, j))
                    seen.add((i, j))
                    while q:
                        for _ in range(len(q)):
                            current = q.popleft()
                            I = current[0]
                            J = current[1]
                            if I + 1 <= iBoundary and (I+1, J) not in seen and board[I+1][J] == "O":
                                q.append((I+1, J))
                                seen.add((I+1, J))
                                curr.append((I+1, J))
                            if J + 1 <= jBoundary and (I, J+1) not in seen and board[I][J+1] == "O":
                                q.append((I, J+1))
                                seen.add((I, J+1))
                                curr.append((I, J+1))
                            if I - 1 >= 0 and (I-1, J) not in seen and board[I-1][J] == "O":
                                q.append((I-1, J))
                                seen.add((I-1, J))
                                curr.append((I-1, J))
                            if J - 1 >= 0 and (I, J-1) not in seen and board[I][J-1] == "O":
                                q.append((I, J-1))
                                seen.add((I, J-1))
                                curr.append((I, J-1))
                    valid = True
                    for point in curr:
                        if point[0] == iBoundary or point[0] == 0 or point[1] == jBoundary or point[1] == 0:
                            valid = False
                            break
                    if valid:
                        replace += curr
        for point in replace:
            board[point[0]][point[1]] = "X"


        