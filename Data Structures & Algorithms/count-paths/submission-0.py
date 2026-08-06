class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo_tb = [[-1] * n for _ in range(m)]

        def helper(r, c):
            if r == m - 1 and c == n - 1:
                return 1
            
            if r >= m or c >= n:
                return 0

            if memo_tb[r][c] != -1:
                return memo_tb[r][c]

            memo_tb[r][c] = helper(r, c + 1) + helper(r + 1, c)

            return memo_tb[r][c]
        
        return helper(0, 0)
