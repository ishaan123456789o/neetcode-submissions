class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = ""
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        maxI = len(board)
        maxJ = len(board[0])
        root = TrieNode()
        for word in words:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                    curr.children[ch].value = ch
                curr = curr.children[ch]
            if '/' not in curr.children:
                curr.children['/'] = TrieNode()
        result = []
        resultSet = set()
        current = root
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in current.children:
                    q = deque()
                    res = ""
                    Seen = set()
                    Seen.add((i, j))
                    res += board[i][j]
                    q.append((i, j, current.children[board[i][j]], res, Seen))
                    while q:
                        for _ in range(len(q)):
                            curr = q.popleft()
                            node = curr[2]
                            I = curr[0]
                            J = curr[1]
                            wordSoFar = curr[3]
                            seen = curr[4]
                            if '/' in node.children and wordSoFar not in resultSet:
                                result.append(wordSoFar)
                                resultSet.add(wordSoFar)
                            if I + 1 < maxI and (I+1, J) not in seen and board[I+1][J] in node.children:
                                q.append((I+1, J, node.children[board[I+1][J]], wordSoFar + board[I+1][J], seen | {(I+1,J)}))
                            if J + 1 < maxJ and (I, J+1) not in seen and board[I][J+1] in node.children:
                                q.append((I, J+1, node.children[board[I][J+1]], wordSoFar + board[I][J+1], seen | {(I,J+1)}))
                            if I - 1 >= 0 and (I-1, J) not in seen and board[I-1][J] in node.children:
                                q.append((I-1, J, node.children[board[I-1][J]], wordSoFar + board[I-1][J], seen | {(I-1,J)}))
                            if J - 1 >= 0 and (I, J-1) not in seen and board[I][J-1] in node.children:
                                q.append((I, J-1, node.children[board[I][J-1]], wordSoFar + board[I][J-1], seen | {(I,J-1)}))


        return result

        