class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        treasure = []
        directions = ((0,1), (0,-1), (1,0), (-1,0))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    treasure.append((row,col))
                
        queue = deque()
        # we want to add the treasures to the queue
        for row,col in treasure:
            queue.append((row,col))
        
        while queue:
            # this will ensure we evaluate treasures at the same time before moving on
            for _ in range(len(queue)):
                cell = queue.popleft()
                row = cell[0]
                col = cell[1]
                for dr,dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 2147483647:
                        queue.append((nr,nc))
                        grid[nr][nc] = grid[row][col] + 1