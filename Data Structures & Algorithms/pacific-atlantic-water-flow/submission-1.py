class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        directions = ((0,1), (0,-1), (1,0), (-1,0))
        output = []

        # for pacific it would be row == 0, or col == 0
        # for atlantic it would be row == len(heights), or col = len(heights[0])

        def dfs(row, col, ocean): # ocean is a set
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if 0 <= nr < len(heights) and 0 <= nc < len(heights[0]) and heights[row][col] <= heights[nr][nc] and (nr,nc) not in ocean:
                    ocean.add((nr,nc))
                    dfs(nr,nc,ocean)

        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if row == 0 or col == 0:
                    pacific.add((row,col))
                    dfs(row,col,pacific)
                if row == len(heights) - 1 or col == len(heights[0]) - 1:
                    atlantic.add((row,col))
                    dfs(row,col,atlantic)
        
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if (row,col) in pacific and (row,col) in atlantic:
                    output.append([row,col])
        
        return output

            