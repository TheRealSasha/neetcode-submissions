class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=m*n)
        def helper(r, c):
            if r == m - 1 and c == n - 1:
                return 1
            
            if r >= m or c >= n:
                return 0
            
            return helper(r + 1, c) + helper(r, c + 1)
        
        return helper(0, 0)

