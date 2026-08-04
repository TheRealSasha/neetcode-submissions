class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # backtracking 
        m, n = len(board), len(board[0])
        visited = set()

        def backtrack(r, c, i):
            if i == len(word):
                return True
            
            if r < 0 or c < 0 or r >= m or c >= n or board[r][c] != word[i] or (r, c) in visited:
                return False

            
            visited.add((r, c))

            flag = backtrack(r + 1, c, i + 1) or backtrack(r, c + 1, i + 1) or backtrack(r - 1, c, i + 1) or backtrack(r, c - 1, i + 1)

            visited.remove((r, c))

            return flag 
        
        for r in range(m):
            for c in range(n):
                if backtrack(r, c, 0):
                    return True
        
        return False








        