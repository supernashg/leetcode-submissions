class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        INF = 2**31 - 1

        q = deque()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j, 0))

        while q:
            i, j, dist = q.popleft()
            for di, dj in dirs:
                r = i + di
                c = j + dj
                if 0 <= r < rows and 0 <= c < cols and grid[r][c] == INF:
                    q.append((r, c, dist + 1))
                    grid[r][c] = dist + 1

        