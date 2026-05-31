class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[m-1][n-1] = 1
        q = deque()
        q.append((m-1, n-1))
        seen = set()
        seen.add((m-1, n-1))
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                i = curr[0]
                j = curr[1]
                if i-1 >= 0:
                    dp[i-1][j] += dp[i][j]
                    if (i-1, j) not in seen:
                        q.append((i-1,j))
                        seen.add((i-1,j))
                if j-1 >= 0:
                    dp[i][j-1] += dp[i][j]
                    if (i, j-1) not in seen:
                        q.append((i, j-1))
                        seen.add((i, j-1))
        return dp[0][0]

        