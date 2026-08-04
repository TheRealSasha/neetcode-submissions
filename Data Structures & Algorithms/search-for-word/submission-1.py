class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # backtracking 
        # time complexity: O(m * n * len(word) ^ 4)
        # space complexity: O(m * n)

        m, n = len(board), len(board[0])

        def backtrack(r, c, i):
            if i == len(word):
                return True
            
            if r < 0 or c < 0 or r >= m or c >= n or board[r][c] != word[i] or board[r][c] == "#":
                return False

            
            temp = board[r][c]
            board[r][c] = "#"

            flag = backtrack(r + 1, c, i + 1) or backtrack(r, c + 1, i + 1) or backtrack(r - 1, c, i + 1) or backtrack(r, c - 1, i + 1)

            board[r][c] = temp

            return flag 
        
        for r in range(m):
            for c in range(n):
                if backtrack(r, c, 0):
                    return True
        
        return False








        