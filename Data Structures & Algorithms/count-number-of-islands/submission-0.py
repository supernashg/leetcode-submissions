class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or (i, j) in visited or grid[i][j] == "0":
                return
            visited.add((i, j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        visited = set()
        num_islands = 0
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == "1":
                    num_islands += 1
                    dfs(i, j)
        return num_islands
