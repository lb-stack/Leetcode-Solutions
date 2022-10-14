class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        visit = set()
        
        def dfs(r,c):
            if (r < 0 or r == num_rows or c < 0 or c == num_cols or grid[r][c] == 0 or (r,c) in visit):
                return 0 
            
            visit.add((r,c))
            
            return (1 + dfs(r + 1, c)+
                        dfs(r - 1, c)+
                        dfs(r, c + 1)+
                        dfs(r, c - 1))
        area = 0
        for r in range(num_rows):
            for c in range(num_cols):
                area = max(area, dfs(r,c))
        return area
