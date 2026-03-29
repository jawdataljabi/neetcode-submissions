class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0 
        fresh = 0
        rotten = []
        directions = ((0,1), (0,-1), (1,0), (-1,0))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    rotten.append([row,col])
                
        # below is where the traversal occurs
        queue = deque()
        for rotted in rotten:
            queue.append(rotted)
        
        while fresh > 0 and queue:
            for _ in range(len(queue)):
                cell = queue.popleft()
                row = cell[0]
                col = cell[1]
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append([nr, nc])
            time += 1
        
        if not fresh:
            return time
        return -1