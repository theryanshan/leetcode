class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(dr + r, dc + c)

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visit:
                    count += 1
                    dfs(i, j)
        return count
