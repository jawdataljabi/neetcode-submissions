class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # run dfs on O's that are on the borded. the border is defined as:
        # row == 0, col == 0, row = len(board), col = len(board[0])
        directions = ((0,1), (0,-1), (1,0), (-1,0))
        keep = set() # the O's that will be kept as O's

        def dfs(row,col):
            keep.add((row,col))
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == "O" and (nr,nc) not in keep:
                    dfs(nr,nc)
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row == 0 or col == 0 or row == len(board) - 1 or col == len(board[0]) - 1) and board[row][col] == "O":
                    dfs(row,col)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O" and (row,col) not in keep:
                    board[row][col] = "X"
        