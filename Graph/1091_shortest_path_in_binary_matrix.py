# Time: O(N^2)
# Space: O(N^2)


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] != 0:
            return -1
        ROWS, COLS = len(grid), len(grid[0])
        length = 1
        queue = collections.deque()
        visited = set()
        queue.append((0, 0))
        visited.add((0, 0))

        while queue:
            for i in range(len(queue)):
                (r, c) = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length

                dirs = [
                    [-1, -1],
                    [-1, 0],
                    [-1, 1],
                    [0, -1],
                    [0, 1],
                    [1, -1],
                    [1, 0],
                    [1, 1],
                ]
                for dr, dc in dirs:
                    row, col = dr + r, dc + c
                    if (
                        row not in range(ROWS)
                        or col not in range(COLS)
                        or (row, col) in visited
                        or grid[row][col] == 1
                    ):
                        continue
                    queue.append((row, col))
                    visited.add((row, col))
            length += 1

        return -1
