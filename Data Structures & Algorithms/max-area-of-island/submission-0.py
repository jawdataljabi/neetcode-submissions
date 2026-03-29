class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        directions = ((0,1), (0,-1), (1,0), (-1,0))

        def traversal(row, col):
            queue = deque()
            queue.append((row,col))
            grid[row][col] = 0
            islandArea = 1

            while queue:
                land = queue.popleft()
                row = land[0]
                col = land[1]
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        queue.append((nr,nc))
                        grid[nr][nc] = 0
                        islandArea += 1
                        
            return islandArea

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area = max(area, traversal(row,col))
        return area
                