def explore(grid, n, i, j):
    if (i + 1 >= n) or (i - 1 < 0) or (j + 1 >= n) or (j - 1 < 0):
        return
    else:
        numbers = [
            grid[i][j],
            grid[i][j + 1],
            grid[i + 1][ j + 1],
            grid[i + 1][ j],
            grid[i + 1][ j - 1],
            grid[i][ j - 1],
            grid[i - 1][ j - 1],
            grid[i - 1][ j],
            grid[i - 1][ j + 1],
        ]
        return max(numbers)


class Solution(object):
    def largestLocal(self, grid):
        n = len(grid)
        m = n - 2
        ans = [[0] * m for _ in range(m)]
        
        for i in range(m):
            for j in range(m):
                ans[i][j] = explore(grid, n, i + 1, j + 1)
                
        return ans


solution = Solution()
grid = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
print(solution.largestLocal(grid))  # [[9,9],[8,6]]
