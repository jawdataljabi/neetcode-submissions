class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = ((0,1), (0,-1), (1,0), (-1,0))

        def dfs(row, col, seen, i, subString):
            if subString == word:
                return True
            
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                
                if (
                    0 <= nr < len(board) and
                    0 <= nc < len(board[0]) and
                    i + 1 < len(word) and
                    board[nr][nc] == word[i + 1] and
                    (nr,nc) not in seen
                ):
                    seen.add((nr,nc))
                    nextString = subString + word[i + 1]
                    
                    if dfs(nr, nc, seen, i + 1, nextString):
                        return True
                    
                    seen.remove((nr,nc)) # backtrack so that other directions can evaluate
                    
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if dfs(row, col, {(row,col)}, 0, word[0]):
                        return True
        return False
