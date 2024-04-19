def explore(grid, m, n, i, j):
    if (i < 0) or (i >= m) or (j < 0) or (j >= n):
        return
    else:
        if grid[i][j] == "1":
            grid[i][j] = "0"
            explore(grid, m, n, i - 1, j)
            explore(grid, m, n, i + 1, j)
            explore(grid, m, n, i, j - 1)
            explore(grid, m, n, i, j + 1)


class Solution(object):
    def numIslands(self, grid):
        counter = 0
        m = len(grid)  # rows
        n = len(grid[0])  # cols

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    counter += 1
                    explore(grid, m, n, i, j)
        return counter


solution = Solution()

grid = grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
print(solution.numIslands(grid))  # 1

grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
print(solution.numIslands(grid2))  # 3
