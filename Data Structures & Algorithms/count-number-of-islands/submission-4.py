class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        directions = ((0,1), (0,-1), (1,0), (-1,0))

        def dfs(grid, row, col):
            queue = deque()
            queue.append((row,col))
            grid[row][col] = "0"

            while queue:
                land = queue.popleft()
                row = land[0]
                col = land[1]

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == "1":
                        queue.append((nr,nc))
                        grid[nr][nc] = "0"
            

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    dfs(grid, row, col)
                    islands += 1

        return islands

