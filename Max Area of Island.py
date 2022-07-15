class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited = set()
        maxCount = 0
        
        def DFS(grid, r, c, visited):
            rowBounds = r >= 0 and r < len(grid)
            colBounds = c >= 0 and c < len(grid[0])

            if not rowBounds or not colBounds:
                return 0

            if grid[r][c] == 0:
                return 0
            
            pos = f"{r},{c}"
            if pos in visited:
                return 0

            visited.add(pos)

            return (1 + DFS(grid, r + 1, c, visited) 
                      + DFS(grid, r, c + 1, visited) 
                      + DFS(grid, r - 1, c, visited)
                      + DFS(grid, r, c - 1, visited))

        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                maxCount = max(DFS(grid, r, c, visited), maxCount)
                
                
        return maxCount
                
