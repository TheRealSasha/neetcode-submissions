class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = dict()

        def helper(r, c):
            if r == m - 1 and c == n - 1:
                return 1
            
            if r >= m or c >= n:
                return 0

            if (r, c) in dp:
                return dp[(r, c)]
            
            dp[(r, c)] = helper(r + 1, c) + helper(r, c + 1)

            return dp[(r, c)]
        
        return helper(0, 0)

