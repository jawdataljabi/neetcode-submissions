class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # have a string to append to for each call
        # base case: if len(string) == len(word) and string != word, then break
        # base case: if string == word, then return True

        directions = ((0,1), (0,-1), (1,0), (-1,0))
        seen = set()

        def dfs(index, row, col, curWord):
            # base case
            if curWord == word:
                return True
            elif len(curWord) == len(word):
                return

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if ( 0 <= nr < len(board) and 
                0 <= nc < len(board[0]) and 
                (nr, nc) not in seen and 
                board[nr][nc] == word[index + 1]
                ):
                    seen.add((nr,nc))
                    newWord = curWord + board[nr][nc]

                    if dfs(index + 1, nr, nc, newWord):
                        return True
                    seen.remove((nr,nc)) # backtrack
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    seen.add((row,col))
                    if dfs(0, row, col, word[0]):
                        return True
                    seen.remove((row,col))
        
        return False


