# Bottom Up
import math


class Solution(object):
    def numSquares(self, n):
        squares = [i**2 for i in range(0, int(math.sqrt(n)) + 1)]
        memo = [float("inf")] * (n + 1)
        memo[0] = 0
        for i in range(0, n + 1):
            for s in squares:
                if i >= s:
                    memo[i] = min(memo[i], memo[i - s] + 1)
        return memo[n]


solution = Solution()
print(solution.numSquares(12))
