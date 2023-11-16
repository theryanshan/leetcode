# Time: O(m * n)
# Space: O(m * n)
# Tip: use DFS to find the area of each island, and update the max area


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if (
                r not in range(ROWS)
                or c not in range(COLS)
                or (r, c) in visited
                or grid[r][c] == 0
            ):
                return 0
            visited.add((r, c))
            DIRS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            area = 1
            for dr, dc in DIRS:
                row, col = dr + r, dc + c
                area += dfs(row, col)
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = dfs(r, c)
                    maxArea = max(maxArea, area)

        return maxArea
